# -*- coding: utf-8 -*-
import copy
import json
from itertools import chain
from operator import itemgetter
import datetime
from collections import OrderedDict

from colour import Color


from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _, get_language, \
    ugettext_noop
from django.core import serializers
from django.db import connection
from django.db.models import Max, Q, Prefetch
from django.utils import formats
from django.utils import timezone
from django.utils import dateformat
from django.urls import reverse
from django.template import defaultfilters
from django.template.loader import get_template

from kiola.kiola_senses import models as senses
from kiola.kiola_senses import const as senses_const
from kiola.kiola_charts import charts as base_charts
from kiola.kiola_charts import utils as charts_utils
from kiola.kiola_charts import const as charts_const

from kiola.cares import charts as cares_charts

from . import models
from . import const

#physical activity
class PAChart(cares_charts.ChartBase):
    category = const.CHART_CATEGORY__PHYSICALACTIVITY
    show_on_dashboard = True
    plots = [base_charts.TimePlot, ]
    root_observations = [const.DAILY_PHYSICAL_ACTIVITY_ROOT, ]
    series = [const.DAILY_VIGOROUS_ACTIVITY,
              const.DAILY_MODERATE_ACTIVITY,
              const.DAILY_SEDENTARY_ACTIVITY,
              ]
    # TODO:cgo: get the colors from configuration
    base_colors = {const.DAILY_VIGOROUS_ACTIVITY: "#910000",
                   const.DAILY_MODERATE_ACTIVITY: "#2f7ed8",
                   const.DAILY_SEDENTARY_ACTIVITY: "#8BBC21",
                   const.DAILY_PHYSICAL_ACTIVITY_ROOT: '#D5D5D5',
                   }

    chart_options = copy.deepcopy(cares_charts.ObservationChart.chart_options)
    chart_options.update({"yAxis": {
        "title": {
            "text": _(const.DAILY_PHYSICAL_ACTIVITY_ROOT),
        },
        #"minRange": 20,
        "min": 0,
    },

        "tooltip": {"useHTML": True
                    }

    })
    ''',
                    "formatter":
                    serializer.RawJavaScriptText("""function (tt) {
                            if (this.series.type.indexOf('columnrange') !== -1) {
                                return false;
                            } else {
                                return tt.defaultFormatter.call(this,tt)
                            }
                        }""")'''

    chart_options["plotOptions"]["columnrange"] = {"grouping": False,
                                                   }

    series_options = [{
        "name": _(const.DAILY_VIGOROUS_ACTIVITY),
        "id": const.DAILY_VIGOROUS_ACTIVITY,
        "lineWidth": 0,
        "color": base_colors[const.DAILY_VIGOROUS_ACTIVITY],
        "marker":{"symbol": "bar",
                  "radius": charts_const.CHART__DEFAULT_MARKER_RADIUS},
        "zIndex": 10
    }, {
        "name": _(const.DAILY_MODERATE_ACTIVITY),
        "id": const.DAILY_MODERATE_ACTIVITY,
        "color": base_colors[const.DAILY_MODERATE_ACTIVITY],
        "lineWidth":0,
        "marker":{"symbol": "bar",
                  "radius": charts_const.CHART__DEFAULT_MARKER_RADIUS},
        "zIndex": 10
    }, {
        "name": _(const.DAILY_SEDENTARY_ACTIVITY),
        "id": const.DAILY_SEDENTARY_ACTIVITY,
        "color": base_colors[const.DAILY_SEDENTARY_ACTIVITY],
        "lineWidth": 0,
        "marker": {"symbol": "circle",
                   "radius": charts_const.CHART__DEFAULT_MARKER_RADIUS},
        "zIndex": 10,
    },
    ]

    """threshold_providers = {"static": cares_charts.StaticThresholdProvider(),
                           "dynamic": cares_charts.DynamicThresholdProvider()}"""

    def __init__(self):
        super(PAChart, self).__init__()

    def get_yaxis_title(self):
        return "%s [%s] / %s [%s]" % "vigurous or moderate", self.get_unit(senses_const.DAILY_VIGOROUS_ACTIVITY), "sedentary", self.get_unit(senses_const.DAILY_SEDENTARY_ACTIVITY)

    def get(self, subject, which, period, ajax=False, data_filters={}):
        """returns the plot"""
        plot = super(PAChart, self).get(subject, which, period, ajax, data_filters)
        chart_options = copy.deepcopy(self.chart_options)

        orig_flt = {'parent__started__range': period, }
        orig_flt.update(data_filters)
        # get chart data for each series
        #bp_data = []
        for counter, series in enumerate(self.series):
            # get all thresholds
            flt = self.update_filter(counter, series, orig_flt, subject)
            self.threshold_providers["dynamic"].apply(plot, series, subject, period, self)

            chart_data = self.get_queryset(counter, series, subject, profile, flt, as_values=True, **kwargs)

            #if series == const.DAILY_MODERATE_ACTIVITY:
            #    bp_data = chart_data.values_list('parent__started', 'value')

            chart_data = self.postprocess_chartdata(counter, series, chart_data)
            # store it for later use

            series_options = copy.deepcopy(self.series_options[counter])
            series_options.update({"tooltip": {
                                  "useHTML": True,
                                  "pointFormat": '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ',
                                  "valueSuffix":  u" {0}".format(self.get_unit(series)),
                                  "crosshairs": True
                                  },
            })
            plot.addSeries(chart_data, series_options)
        chart_options = copy.deepcopy(self.chart_options)

        self.update_axis(plot)

        # FIXME:cgo: make this configurable
        idx, s = plot.get_series_by_id(const.DAILY_VIGOROUS_ACTIVITY)
        if idx is not None:
            series_options = copy.deepcopy(charts_const.CHART__DEFAULT_MOVING_M_SERIES_OPTIONS)
            series_options["name"] = _("{0}_MEDIAN".format(const.DAILY_VIGOROUS_ACTIVITY))
            stat_extensions.add_moving_median(plot, plot.datasources[idx],
                                              series_options=series_options)

        idx, s = plot.get_series_by_id(const.DAILY_MODERATE_ACTIVITY)
        if idx is not None:
            series_options = copy.deepcopy(charts_const.CHART__DEFAULT_MOVING_M_SERIES_OPTIONS)
            series_options["name"] = _("{0}_MEDIAN".format(const.DAILY_MODERATE_ACTIVITY))
            stat_extensions.add_moving_median(plot, plot.datasources[idx],
                                              series_options=series_options)

        idx, s = plot.get_series_by_id(const.DAILY_SEDENTARY_ACTIVITY)
        if idx is not None:
            series_options = copy.deepcopy(charts_const.CHART__DEFAULT_MOVING_M_SERIES_OPTIONS)
            series_options["name"] = _("{0}_MEDIAN".format(const.DAILY_SEDENTARY_ACTIVITY))
            stat_extensions.add_moving_median(plot, plot.datasources[idx],
                                              series_options=series_options)

        plot.updateOptions(chart_options)
        self.set_comment_tooltip_handler(plot)

        return plot

#time range? accurate to minutes
class SleepChart(cares_charts.ObservationChart):
    category = const.CHART_CATEGORY__SLEEP
    show_on_dashboard = True
    plots = [base_charts.TimePlot, ]
    root_observations = [const.DAILY_SLEEP_ROOT, ]
    series = [const.DAILY_BED_TIME,
              const.DAILY_ASLEEP_TIME,
              const.DAILY_WAKEUP_TIME,
              ]

    base_colors = {const.DAILY_BED_TIME: "#910000",
                   const.DAILY_ASLEEP_TIME: "#2f7ed8",
                   const.DAILY_WAKEUP_TIME: "#8BBC21",
                   const.DAILY_SLEEP_ROOT: '#D5D5D5',
                   }

    chart_options = copy.deepcopy(cares_charts.ObservationChart.chart_options)
    chart_options.update({"yAxis": {
        "title": {
            "text": _(const.DAILY_SLEEP_ROOT),
        },
        #"minRange": 20,
        "min": 0,
    },

        "tooltip": {"useHTML": True
                    }

    })

    chart_options["plotOptions"]["columnrange"] = {"grouping": False,
                                                   }

    series_options = [{
        "name": _(const.DAILY_BED_TIME),
        "id": const.DAILY_BED_TIME,
        "lineWidth": 0,
        "color": base_colors[const.DAILY_BED_TIME],
        "marker":{"symbol": "bar",
                  "radius": charts_const.CHART__DEFAULT_MARKER_RADIUS},
        "zIndex": 10
    }, {
        "name": _(const.DAILY_ASLEEP_TIME),
        "id": const.DAILY_ASLEEP_TIME,
        "color": base_colors[const.DAILY_ASLEEP_TIME],
        "lineWidth":0,
        "marker":{"symbol": "bar",
                  "radius": charts_const.CHART__DEFAULT_MARKER_RADIUS},
        "zIndex": 10
    }, {
        "name": _(const.DAILY_WAKEUP_TIME),
        "id": const.DAILY_WAKEUP_TIME,
        "color": base_colors[const.DAILY_WAKEUP_TIME],
        "lineWidth": 0,
        "marker": {"symbol": "circle",
                   "radius": charts_const.CHART__DEFAULT_MARKER_RADIUS},
        "zIndex": 10,
    },
    ]

    threshold_providers = {"static": cares_charts.StaticThresholdProvider(),
                           "dynamic": cares_charts.DynamicThresholdProvider()}

    def __init__(self):
        super(SleepChart, self).__init__()

    def get_yaxis_title(self):
        return "%s [%s]" % "sleep activity time", self.get_unit(senses_const.DAILY_BED_TIME)

    def get(self, subject, which, period, ajax=False, data_filters={}, **kwargs):
        """returns the plot"""
        if which not in self.plots:
            raise AttributeError("Plot %s not defined for chart %s" % (which, self.__class__.__name__))
        plot = which()
        self._localize(plot, period)
        orig_flt = {'parent__started__range': period, }
        orig_flt.update(data_filters)
        for counter, series in enumerate(self.series):
            flt = self.update_filter(counter, series, orig_flt, subject)
            self.threshold_providers["dynamic"].apply(plot, series, subject, period, self)

            profile = senses.ObservationProfile.objects.get_profile(name=series)

            chart_data = self.get_queryset(counter, series, subject, profile, flt, as_values=True, **kwargs)

            chart_data = self.postprocess_chartdata(counter, series, chart_data)

            series_options = copy.deepcopy(self.series_options[counter])
            series_options.update({"tooltip": {
                                  "useHTML": True,
                                  "pointFormat": '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ',
                                  "valueSuffix":  u" {0}".format(self.get_unit(series)),
                                  "crosshairs": True
                                  },
            })
            plot.addSeries(chart_data, series_options)
        chart_options = copy.deepcopy(self.chart_options)

        self.update_axis(plot)

        # FIXME:cgo: make this configurable
        idx, s = plot.get_series_by_id(const.DAILY_BED_TIME)
        if idx is not None:
            series_options = copy.deepcopy(charts_const.CHART__DEFAULT_MOVING_M_SERIES_OPTIONS)
            series_options["name"] = _("{0}_MEDIAN".format(const.DAILY_BED_TIME))
            stat_extensions.add_moving_median(plot, plot.datasources[idx],
                                              series_options=series_options)

        idx, s = plot.get_series_by_id(const.DAILY_ASLEEP_TIME)
        if idx is not None:
            series_options = copy.deepcopy(charts_const.CHART__DEFAULT_MOVING_M_SERIES_OPTIONS)
            series_options["name"] = _("{0}_MEDIAN".format(const.DAILY_ASLEEP_TIME))
            stat_extensions.add_moving_median(plot, plot.datasources[idx],
                                              series_options=series_options)

        idx, s = plot.get_series_by_id(const.DAILY_WAKEUP_TIME)
        if idx is not None:
            series_options = copy.deepcopy(charts_const.CHART__DEFAULT_MOVING_M_SERIES_OPTIONS)
            series_options["name"] = _("{0}_MEDIAN".format(const.DAILY_WAKEUP_TIME))
            stat_extensions.add_moving_median(plot, plot.datasources[idx],
                                              series_options=series_options)

        plot.updateOptions(chart_options)
        self.set_comment_tooltip_handler(plot)

        return plot

#weekly/monthly healthscore
"""
class HealthScoreChart(cares_charts.ObservationChart):
    category = const.CHART_CATEGORY__HEALTHSCORE
    show_on_dashboard = True
    plots = [base_charts.TimePlot, ]
    root_observations = [const.HEALTSCORE_ROOT, ]
    series = [const.WELLBEING_SCORE,
              const.DIET_SCORE,
              const.ALCOHOL_SMOKING_SCORE,
              const.PA_SCORE,
              const.SLEEP_SCORE,
              const.FINAL_HEALTHSCORE,
              ]

    base_colors = {const.WELLBEING_SCORE: "#910000",
                   const.DIET_SCORE: "#2f7ed8",
                   const.ALCOHOL_SMOKING_SCORE: "#8BBC21",
                   const.PA_SCORE: "#B74635",
                   const.SLEEP_SCORE: "#428BCA",
                   const.FINAL_HEALTHSCORE: "green",
                   const.HEALTSCORE_ROOT: '#D5D5D5',
                   }

    chart_options = copy.deepcopy(cares_charts.ObservationChart.chart_options)
    chart_options.update({"yAxis": {
        "title": {
            "text": _(const.HEALTSCORE_ROOT),
        },
        "minRange": 10,
        "min": 0,
    },

        "tooltip": {"useHTML": True
                    }

    })

    chart_options["plotOptions"]["columnrange"] = {"grouping": False,
                                                   }

    series_options = [{
        "name": _(const.WELLBEING_SCORE),
        "id": const.WELLBEING_SCORE,
        "lineWidth": 0,
        "color": base_colors[const.WELLBEING_SCORE],
        "marker":{"symbol": "bar",
                  "radius": charts_const.CHART__DEFAULT_MARKER_RADIUS},
        "zIndex": 10
    }, {
        "name": _(const.DIET_SCORE),
        "id": const.DIET_SCORE,
        "color": base_colors[const.DIET_SCORE],
        "lineWidth":0,
        "marker":{"symbol": "bar",
                  "radius": charts_const.CHART__DEFAULT_MARKER_RADIUS},
        "zIndex": 10
    }, {
        "name": _(const.ALCOHOL_SMOKING_SCORE),
        "id": const.ALCOHOL_SMOKING_SCORE,
        "color": base_colors[const.ALCOHOL_SMOKING_SCORE],
        "lineWidth": 0,
        "marker": {"symbol": "circle",
                   "radius": charts_const.CHART__DEFAULT_MARKER_RADIUS},
        "zIndex": 10,
    },{
        "name": _(const.PA_SCORE),
        "id": const.PA_SCORE,
        "color": base_colors[const.PA_SCORE],
        "lineWidth": 0,
        "marker": {"symbol": "circle",
                   "radius": charts_const.CHART__DEFAULT_MARKER_RADIUS},
        "zIndex": 10,
    },{
        "name": _(const.SLEEP_SCORE),
        "id": const.SLEEP_SCORE,
        "color": base_colors[const.SLEEP_SCORE],
        "lineWidth": 0,
        "marker": {"symbol": "circle",
                   "radius": charts_const.CHART__DEFAULT_MARKER_RADIUS},
        "zIndex": 10,
    },{
        "name": _(const.FINAL_HEALTHSCORE),
        "id": const.FINAL_HEALTHSCORE,
        "color": base_colors[const.FINAL_HEALTHSCORE],
        "lineWidth": 0,
        "marker": {"symbol": "circle",
                   "radius": charts_const.CHART__DEFAULT_MARKER_RADIUS},
        "zIndex": 20,
    },
    ]

    threshold_providers = {"static": cares_charts.StaticThresholdProvider(),
                           "dynamic": cares_charts.DynamicThresholdProvider()}

    def __init__(self):
        super(SleepChart, self).__init__()

    def get_yaxis_title(self):
        return "%s" % "Health score"

    def get(self, subject, which, period, ajax=False, data_filters={}, **kwargs):
        if which not in self.plots:
            raise AttributeError("Plot %s not defined for chart %s" % (which, self.__class__.__name__))
        plot = which()
        self._localize(plot, period)
        orig_flt = {'parent__started__range': period, }
        orig_flt.update(data_filters)
        for counter, series in enumerate(self.series):
            flt = self.update_filter(counter, series, orig_flt, subject)
            self.threshold_providers["dynamic"].apply(plot, series, subject, period, self)

            profile = senses.ObservationProfile.objects.get_profile(name=series)

            chart_data = self.get_queryset(counter, series, subject, profile, flt, as_values=True, **kwargs)

            chart_data = self.postprocess_chartdata(counter, series, chart_data)

            series_options = copy.deepcopy(self.series_options[counter])
            series_options.update({"tooltip": {
                                  "useHTML": True,
                                  "pointFormat": '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ',
                                  "valueSuffix":  u" {0}".format(self.get_unit(series)),
                                  "crosshairs": True
                                  },
            })
            plot.addSeries(chart_data, series_options)
        chart_options = copy.deepcopy(self.chart_options)

        self.update_axis(plot)
        idx, s = plot.get_series_by_id(const.WELLBEING_SCORE)
        if idx is not None:
            series_options = copy.deepcopy(charts_const.CHART__DEFAULT_MOVING_M_SERIES_OPTIONS)
            series_options["name"] = _("{0}_MEDIAN".format(const.WELLBEING_SCORE))
            stat_extensions.add_moving_median(plot, plot.datasources[idx],
                                              series_options=series_options)

        idx, s = plot.get_series_by_id(const.DIET_SCORE)
        if idx is not None:
            series_options = copy.deepcopy(charts_const.CHART__DEFAULT_MOVING_M_SERIES_OPTIONS)
            series_options["name"] = _("{0}_MEDIAN".format(const.DIET_SCORE))
            stat_extensions.add_moving_median(plot, plot.datasources[idx],
                                              series_options=series_options)

        idx, s = plot.get_series_by_id(const.ALCOHOL_SMOKING_SCORE)
        if idx is not None:
            series_options = copy.deepcopy(charts_const.CHART__DEFAULT_MOVING_M_SERIES_OPTIONS)
            series_options["name"] = _("{0}_MEDIAN".format(const.ALCOHOL_SMOKING_SCORE))
            stat_extensions.add_moving_median(plot, plot.datasources[idx],
                                              series_options=series_options)
        
        idx, s = plot.get_series_by_id(const.PA_SCORE)
        if idx is not None:
            series_options = copy.deepcopy(charts_const.CHART__DEFAULT_MOVING_M_SERIES_OPTIONS)
            series_options["name"] = _("{0}_MEDIAN".format(const.PA_SCORE))
            stat_extensions.add_moving_median(plot, plot.datasources[idx],
                                              series_options=series_options)
        
        idx, s = plot.get_series_by_id(const.SLEEP_SCORE)
        if idx is not None:
            series_options = copy.deepcopy(charts_const.CHART__DEFAULT_MOVING_M_SERIES_OPTIONS)
            series_options["name"] = _("{0}_MEDIAN".format(const.SLEEP_SCORE))
            stat_extensions.add_moving_median(plot, plot.datasources[idx],
                                              series_options=series_options)

        idx, s = plot.get_series_by_id(const.FINAL_HEALTHSCORE)
        if idx is not None:
            series_options = copy.deepcopy(charts_const.CHART__DEFAULT_MOVING_M_SERIES_OPTIONS)
            series_options["name"] = _("{0}_MEDIAN".format(const.FINAL_HEALTHSCORE))
            stat_extensions.add_moving_median(plot, plot.datasources[idx],
                                              series_options=series_options)


        plot.updateOptions(chart_options)
        self.set_comment_tooltip_handler(plot)

        return plot

class HSSimpleChart(HealthScoreChart):

    series = [const.FINAL_HEALTHSCORE,
              ]

    base_colors = copy.deepcopy(HealthScoreChart.base_colors)
    series_options = copy.deepcopy(HealthScoreChart.series_options)

    def get_yaxis_title(self):
        return "%s" % (_(senses_const.HEALTSCORE_ROOT))"""


charts_utils.chart_registry.register(PAChart)
charts_utils.chart_registry.register(SleepChart)
"""
charts_utils.chart_registry.register(HealthScoreChart)
charts_utils.chart_registry.register(HSSimpleChart, const.CHART_NAME__SIMPLE_HS_CHART)"""