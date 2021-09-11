#questions:
#how to deal with optional questions
#what is the use of choices? for multiple choices answer? 
#how to link profiles? (with root profiles) each module has one root? and each root connects to each question observation profile? 
#how to represent the options with the need of customer input? e.g. one of the options is: Don't smoke now, but used to. Approximate date stopped smoking [month, year] (date type?)
#for optional questions, is the only diff with normal questions(required an answer) the num_occurances zero one more.
#any efficient way to loop through all multiple choice quesiton with same answers. Wellbeing q2 q3
#backup database sqlite file (copy and paste)
#addtofrontend

#questions after finish writting surveys codes
#ask Rain: repeated same enumeration option type
# ex: "bothered_frequency_option_enum" 
#ask Gyan about questions q3 under demo module

#tbc:
#use postman to test it
#start the charting feature
#high chart
#workshop chart


from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import translation
from django.utils.translation import ugettext_lazy as _, ugettext_noop
from django.contrib.contenttypes.models import ContentType

from kiola.utils.pyxtures import Pyxture as BasePyxture

from kiola.kiola_senses import const as senses_const
from kiola.kiola_senses import models as senses_models
from kiola.cares import const as cares_const

from . import const

class Pyxture(BasePyxture):

    def default(self):
        self.baseline_demo()
        self.baseline_smoking()
        self.baseline_alcohol()
        self.baseline_diet()
        self.baseline_physical_activity()
        self.baseline_sleep()
        self.baseline_health()
        self.baseline_wellbeing()
        self.daily_wellbeing()
        self.daily_diet()
        self.daily_alcohol_smoking()
        self.daily_physical_activity()
        self.daily_sleep()
        self.daily_work()
        
        self.healthscore()
    
    def dev(self):
        self.baseline_demo()
        self.baseline_smoking()
        self.baseline_alcohol()
        self.baseline_diet()
        self.baseline_physical_activity()
        self.baseline_sleep()
        self.baseline_health()
        self.baseline_wellbeing()
        self.daily_wellbeing()
        self.daily_diet()
        self.daily_alcohol_smoking()
        self.daily_physical_activity()
        self.daily_sleep()
        self.daily_work()

        self.healthscore()

    def baseline_demo(self):
        root, _ = senses_models.ObservationProfile.objects.get_or_create_root_profile()

        #----baseline_demo---
        demo_root, _ = senses_models.ExtensibleRootObservationProfile.objects.get_or_create(
            name=const.DEMO_ROOT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=root,
            child=demo_root,
            num_occurences=senses_const.ZERO_OR_MORE
        )

        time_profile = senses_models.DateTimeObservationProfile.objects.get(
            name=senses_const.MDC_ATTR_TIME_ABS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=demo_root, child=time_profile, num_occurences=senses_const.ONE
        )

        #q1 occupation
        occupation_choices = [] + const.MDC_DEMO_OPTION_CHOICE_ENUM_OCCUPATION
        occupation_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.MDC_DEMO_OCCUPATION_OPTION_TYPE,
            values = [
                (
                    "en",
                    occupation_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        occupation_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.MDC_DEMO_OCCUPATION_OPTION, enum_type=occupation_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=demo_root, 
            child=occupation_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        #Number of days
        working_days, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.WORKING_DAYS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=demo_root,
            child=working_days,
            num_occurences=senses_const.ONE
        )
        #q3 tbc

        #shift work
        shifted_work, _ = senses_models.BooleanObservationProfile.objects.get_or_create(
            name=const.SHIFTED_WORK
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=demo_root,
            child=shifted_work,
            num_occurences=senses_const.ONE
        )

        #optional type of shift
        shift_type_choices = [] + const.MDC_DEMO_OPTION_CHOICE_ENUM_SHIFT_TYPE
        shift_type_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.SHIFT_TYPE_OPTION_TYPE,
            values = [
                (
                    "en", shift_type_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        shift_type_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.SHIFT_TYPE_OPTION, enum_type=shift_type_option_enum
        )
        #print(const.MDC_DEMO_OPTION_CHOICE_ENUM_SHIFT_TYPE)

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=demo_root, 
            child=shift_type_option,
            num_occurences=senses_const.ONE_OR_MORE
        )
        
        #age
        age, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.AGE
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=demo_root,
            child=age,
            num_occurences=senses_const.ONE
        )

        #gender
        gender_choices = [] + const.MDC_DEMO_OPTION_CHOICE_ENUM_GENDER
        gender_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.GENDER_OPTION_TYPE,
            values = [
                (
                    "en", gender_choices
                )
            ],
            #use_internal_name_scheme=False,
        )
        gender_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.GENDER_OPTION, enum_type=gender_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=demo_root, 
            child=gender_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        #height decimal
        height, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.HEIGHT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=demo_root,
            child=height,
            num_occurences=senses_const.ONE
        )

        #weight decimal
        weight, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.WEIGHT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=demo_root,
            child=weight,
            num_occurences=senses_const.ONE
        )

        senses_models.ObservationProfile.objects.activate(const.DEMO_ROOT)

        self._add_frontends_to_profile(demo_root)
        for profile in senses_models.ObservationProfile.objects.all():
            #print(profile)
            self._add_frontends_to_profile(profile)


    def baseline_smoking(self):
        root, _ = senses_models.ObservationProfile.objects.get_or_create_root_profile()

        #----baseline_smoking---
        smoking_root, _ = senses_models.ExtensibleRootObservationProfile.objects.get_or_create(
            name=const.SMOKING_ROOT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=root,
            child=smoking_root,
            num_occurences=senses_const.ZERO_OR_MORE
        )

        time_profile = senses_models.DateTimeObservationProfile.objects.get(
            name=senses_const.MDC_ATTR_TIME_ABS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=smoking_root, child=time_profile, num_occurences=senses_const.ONE
        )

        #smoking status options
        smoking_status_choices = [] + const.MDC_SMOKING_OPTION_CHOICE_ENUM_SMOKING_STATUS
        smoking_status_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.SMOKING_STATUS_OPTION_TYPE,
            values = [
                (
                    "en", smoking_status_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        smoking_status_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.SMOKING_STATUS_OPTION, enum_type=smoking_status_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=smoking_root, 
            child=smoking_status_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        #another observation profile for the answer in the options
        #Approximate date stopped smoking [ month, year]
        date_stopped_smoking, _ = senses_models.TextObservationProfile.objects.get_or_create(
            name=const.MDC_ATTR_DATE_STOPPED_SMOKING
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=smoking_root,
            child=date_stopped_smoking,
            num_occurences=senses_const.ZERO_OR_MORE
        )
        

        ##of cigarettes per day
        cigs_per_day_choices = [] + const.MDC_SMOKING_OPTION_CHOICE_ENUM_CIGS_PER_DAY
        cigs_per_day_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.CIGS_PER_DAY_OPTION_TYPE,
            values = [
                (
                    "en", cigs_per_day_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        cigs_per_day_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.CIGS_PER_DAY_OPTION, enum_type=cigs_per_day_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=smoking_root, 
            child=cigs_per_day_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        #frequency of using electronic cigarettes
        frequency_choices = [] + const.MDC_SMOKING_OPTION_CHOICE_ENUM_FREQUENCY
        frequency_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.FREQUENCY_OPTION_TYPE,
            values = [
                (
                    "en", frequency_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        frequency_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.FREQUENCY_OPTION, enum_type=frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=smoking_root, 
            child=frequency_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        senses_models.ObservationProfile.objects.activate(const.SMOKING_ROOT)

        self._add_frontends_to_profile(smoking_root)
        for profile in senses_models.ObservationProfile.objects.all():
            self._add_frontends_to_profile(profile)
        

    def baseline_alcohol(self):
        root, _ = senses_models.ObservationProfile.objects.get_or_create_root_profile()

        #----baseline_alcohol---
        alcohol_root, _ = senses_models.ExtensibleRootObservationProfile.objects.get_or_create(
            name=const.ALCOHOL_ROOT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=root,
            child=alcohol_root,
            num_occurences=senses_const.ZERO_OR_MORE
        )

        time_profile = senses_models.DateTimeObservationProfile.objects.get(
            name=senses_const.MDC_ATTR_TIME_ABS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=alcohol_root, child=time_profile, num_occurences=senses_const.ONE
        )

        ##of days each week
        drink_days_choices = [] + const.MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS
        drink_days_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.DRINK_DAYS_OPTION_TYPE,
            values = [
                (
                    "en", drink_days_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        drink_days_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.DRINK_DAYS_OPTION, enum_type=drink_days_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=alcohol_root, 
            child=drink_days_option,
            num_occurences=senses_const.ONE
        )

        #date stopped drining alcohol
        date_stopped_alcohol, _ = senses_models.TextObservationProfile.objects.get_or_create(
            name=const.MDC_ATTR_DATE_STOPPED_ALCOHOL
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=alcohol_root,
            child=date_stopped_alcohol,
            num_occurences=senses_const.ZERO_OR_MORE
        )
        

        #standard of drinks
        standard_choices = [] + const.MDC_ALCOHOL_OPTION_CHOICE_ENUM_STANDARD
        standard_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.STANDARD_OPTION_TYPE,
            values = [
                (
                    "en", standard_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        standard_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.STANDARD_OPTION, enum_type=standard_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=alcohol_root,
            child=standard_option,
            num_occurences=senses_const.ZERO_OR_MORE
        )
        #number of drinks for alcohol
        num_drinks, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.NUM_DRINKS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=alcohol_root,
            child=num_drinks,
            num_occurences=senses_const.ZERO_OR_MORE
        )

        senses_models.ObservationProfile.objects.activate(const.ALCOHOL_ROOT)

        self._add_frontends_to_profile(alcohol_root)
        for profile in senses_models.ObservationProfile.objects.all():
            self._add_frontends_to_profile(profile)


    def baseline_diet(self):
        root, _ = senses_models.ObservationProfile.objects.get_or_create_root_profile()

        #----baseline_diet---
        diet_root, _ = senses_models.ExtensibleRootObservationProfile.objects.get_or_create(
            name=const.DIET_ROOT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=root,
            child=diet_root,
            num_occurences=senses_const.ZERO_OR_MORE
        )

        #never eat (tick multiples)
        never_eat_choices = [] + const.MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT
        never_eat_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.NEVER_EAT_OPTION_TYPE,
            values = [
                (
                    "en", never_eat_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        never_eat_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.NEVER_EAT_OPTION, enum_type=never_eat_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=never_eat_option,
            num_occurences=senses_const.ZERO_OR_MORE
        )

        #serves of cooked veges
        serves_of_cooked_veges, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.SERVES_OF_COOKED_VEGES
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=serves_of_cooked_veges,
            num_occurences=senses_const.ZERO_OR_ONE
        )

        #serves of raw veges
        serves_of_raw_veges, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.SERVES_OF_RAW_VEGES
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=serves_of_raw_veges,
            num_occurences=senses_const.ZERO_OR_ONE
        )

        #serves of fruit
        serves_of_fruit, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.SERVES_OF_FRUIT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=serves_of_fruit,
            num_occurences=senses_const.ZERO_OR_ONE
        )

        #serves of fruit juice
        serves_of_fruit_juice, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.SERVES_OF_FRUIT_JUICE
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=serves_of_fruit_juice,
            num_occurences=senses_const.ZERO_OR_ONE
        )

        #times eat Beef/lamb/pork
        times_eat_blp, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.TIMES_EAT_BLP
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=times_eat_blp,
            num_occurences=senses_const.ZERO_OR_ONE
        )

        #times eat Chicken/turkey/duck
        times_eat_ctd, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.TIMES_EAT_CTD
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=times_eat_ctd,
            num_occurences=senses_const.ZERO_OR_ONE
        )

        #times eat Processed meat (such as bacon, sausages, salami, devon, burgers, etc)
        times_eat_proc_meat, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.TIMES_EAT_PROC_MEAT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=times_eat_proc_meat,
            num_occurences=senses_const.ZERO_OR_ONE
        )

        #times eat fish/seafood
        times_eat_fish_seafood, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.TIMES_EAT_FISH_SEAFOOD
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=times_eat_fish_seafood,
            num_occurences=senses_const.ZERO_OR_ONE
        )

        #times eat cheese
        times_eat_cheese, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.TIMES_EAT_CHEESE
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=times_eat_cheese,
            num_occurences=senses_const.ZERO_OR_ONE
        )

        #eat how many Slices/pieces of brown/wholemeal bread [ ] per day
        brown_bread, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.BROWN_BREAD
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=brown_bread,
            num_occurences=senses_const.ZERO_OR_ONE
        )

        #eat how many Bowls of breakfast cereal per day
        brekky_cereal, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.BREKKY_CEREAL
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=brekky_cereal,
            num_occurences=senses_const.ZERO_OR_ONE
        )

        #type of brekky cereal
        brekky_cereal_choices = [] + const.MDC_DIET_OPTION_CHOICE_ENUM_BREKKY_CEREAL
        brekky_cereal_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.BREKKY_CEREAL_OPTION_TYPE,
            values = [
                (
                    "en", brekky_cereal_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        brekky_cereal_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.BREKKY_CEREAL_OPTION, enum_type=brekky_cereal_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=brekky_cereal_option,
            num_occurences=senses_const.ZERO_OR_MORE
        )

        #type of milk
        milk_choices = [] + const.MDC_DIET_OPTION_CHOICE_ENUM_MILK
        milk_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.MILK_OPTION_TYPE,
            values = [
                (
                    "en", milk_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        milk_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.MILK_OPTION, 
            enum_type=milk_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=milk_option,
            num_occurences=senses_const.ZERO_OR_MORE
        )

        #sweetened drinks with sugar
        drinks_with_sugar, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.DRINKS_WITH_SUGAR
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=drinks_with_sugar,
            num_occurences=senses_const.ONE
        )

        #sweetened drinks without sugar
        drinks_without_sugar, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.DRINKS_WITHOUT_SUGAR
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=drinks_without_sugar,
            num_occurences=senses_const.ONE
        )

        #caffeine drinks
        caffeine_drinks, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.CAFFEINE_DRINKS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=caffeine_drinks,
            num_occurences=senses_const.ONE
        )

        #frequency of fast food meals
        fast_food_meals, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.FAST_FOOD_MEALS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=fast_food_meals,
            num_occurences=senses_const.ONE
        )

        #fried food
        fried_food, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.FRIED_FOOD
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=fried_food,
            num_occurences=senses_const.ONE
        )

        #twisties or chips
        twisties_chips, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.TWISTIES_CHIPS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=twisties_chips,
            num_occurences=senses_const.ONE
        )

        #sweet snacks
        sweet_snacks, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.SWEET_SNACKS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=sweet_snacks,
            num_occurences=senses_const.ONE
        )

        #confectionary
        confectionary, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.CONFECTIONARY
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=diet_root,
            child=confectionary,
            num_occurences=senses_const.ONE
        )

        senses_models.ObservationProfile.objects.activate(const.DIET_ROOT)

        self._add_frontends_to_profile(diet_root)
        for profile in senses_models.ObservationProfile.objects.all():
            self._add_frontends_to_profile(profile)

    def baseline_physical_activity(self):
        root, _ = senses_models.ObservationProfile.objects.get_or_create_root_profile()

        #----baseline_physical_activity---
        physical_activity_root, _ = senses_models.ExtensibleRootObservationProfile.objects.get_or_create(
            name=const.PHYSICAL_ACTIVITY_ROOT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=root,
            child=physical_activity_root,
            num_occurences=senses_const.ZERO_OR_MORE
        )

        #activity at work
        #working intesity
        intense_work, _ = senses_models.BooleanObservationProfile.objects.get_or_create(
            name=const.INTENSE_WORK
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=physical_activity_root,
            child=intense_work,
            num_occurences=senses_const.ONE
        )

        #frequency of intense work per week
        work_frequency, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.WORK_FREQUENCY
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=physical_activity_root,
            child=work_frequency,
            num_occurences=senses_const.ZERO_OR_ONE
        )

        #time spent per day hrs mins
        #how to represent [ hrs mins] answers
        time_spent, _ = senses_models.TextObservationProfile.objects.get_or_create(
            name=const.MDC_ATTR_TIME_SPENT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=physical_activity_root,
            child=time_spent,
            num_occurences=senses_const.ZERO_OR_ONE
        )
        
        #Travel to and From Places
        #by bicycle
        bicycle_transport, _ = senses_models.BooleanObservationProfile.objects.get_or_create(
            name=const.BICYCLE_TRANSPORT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=physical_activity_root,
            child=bicycle_transport,
            num_occurences=senses_const.ONE
        )

        #days using bicycle
        days_transport, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.DAYS_TRANSPORT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=physical_activity_root,
            child=days_transport,
            num_occurences=senses_const.ZERO_OR_ONE
        )

        #time exercise
        time_transport, _ = senses_models.TextObservationProfile.objects.get_or_create(
            name=const.MDC_ATTR_TIME_TRANSPORT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=physical_activity_root,
            child=time_transport,
            num_occurences=senses_const.ZERO_OR_ONE
        )

        #recreational activities
        do_exercise, _ = senses_models.BooleanObservationProfile.objects.get_or_create(
            name=const.DO_EXERCISE
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=physical_activity_root,
            child=do_exercise,
            num_occurences=senses_const.ONE
        )

        #days exercise
        days_exercise, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.DAYS_EXERCISE
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=physical_activity_root,
            child=days_exercise,
            num_occurences=senses_const.ZERO_OR_ONE
        )

        #time exercise
        time_exercise, _ = senses_models.TextObservationProfile.objects.get_or_create(
            name=const.MDC_ATTR_TIME_EXERCISE
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=physical_activity_root,
            child=time_exercise,
            num_occurences=senses_const.ZERO_OR_ONE
        )

        #sedentary behaviour
        time_sitting_reclining, _ = senses_models.TextObservationProfile.objects.get_or_create(
            name=const.MDC_ATTR_TIME_SITTING_RECLINING
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=physical_activity_root,
            child=time_sitting_reclining,
            num_occurences=senses_const.ONE
        )

        senses_models.ObservationProfile.objects.activate(const.PHYSICAL_ACTIVITY_ROOT)

        #models.RelatedObservationProfile.objects.filter
        self._add_frontends_to_profile(physical_activity_root)
        for profile in senses_models.ObservationProfile.objects.all():
            self._add_frontends_to_profile(profile)


    def baseline_sleep(self):
        root, _ = senses_models.ObservationProfile.objects.get_or_create_root_profile()

        #----baseline_physical_activity---
        sleep_root, _ = senses_models.ExtensibleRootObservationProfile.objects.get_or_create(
            name=const.SLEEP_ROOT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=root,
            child=sleep_root,
            num_occurences=senses_const.ZERO_OR_MORE
        )
        
        #on work days
        #bed time
        work_bed_time, _ = senses_models.TextObservationProfile.objects.get_or_create(
            name=const.MDC_ATTR_WORK_BED_TIME
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=sleep_root,
            child=work_bed_time,
            num_occurences=senses_const.ONE
        )
        
        #number of min
        work_min_fall_asleep, _  = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.WORK_MIN_FALL_ASLEEP
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=sleep_root,
            child=work_min_fall_asleep,
            num_occurences=senses_const.ONE
        )

        #getting up time
        work_get_up_time, _ = senses_models.TextObservationProfile.objects.get_or_create(
            name=const.MDC_ATTR_WORK_GET_UP_TIME
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=sleep_root,
            child=work_get_up_time,
            num_occurences=senses_const.ONE
        )

        #hours of sleep per night
        work_sleeping_hours, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.WORK_SLEEPING_HOURS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=sleep_root,
            child=work_sleeping_hours,
            num_occurences=senses_const.ONE
        )

        #free non working days
        #bed time
        free_bed_time, _ = senses_models.TextObservationProfile.objects.get_or_create(
            name=const.MDC_ATTR_FREE_BED_TIME
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=sleep_root,
            child=free_bed_time,
            num_occurences=senses_const.ONE
        )
        
        #number of min
        free_min_fall_asleep, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.FREE_MIN_FALL_ASLEEP
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=sleep_root,
            child=free_min_fall_asleep,
            num_occurences=senses_const.ONE
        )

        #getting up time
        free_get_up_time, _ = senses_models.TextObservationProfile.objects.get_or_create(
            name=const.MDC_ATTR_FREE_GET_UP_TIME
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=sleep_root,
            child=free_get_up_time,
            num_occurences=senses_const.ONE
        )

        #hours of sleep per night
        free_sleeping_hours, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.FREE_SLEEPING_HOURS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=sleep_root,
            child=free_sleeping_hours,
            num_occurences=senses_const.ONE
        )

        #cannot sleep within 30 min
        cannot_sleep_choices = [] + const.MDC_SLEEP_OPTION_CHOICE_ENUM_CANNOT_SLEEP
        cannot_sleep_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.CANNOT_SLEEP_OPTION_TYPE,
            values = [
                (
                    "en", cannot_sleep_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        cannot_sleep_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.CANNOT_SLEEP_OPTION, 
            enum_type=cannot_sleep_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=sleep_root,
            child=cannot_sleep_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        #wake up in the middle of the night or early in the morning
        unstable_sleep_choices = [] + const.MDC_SLEEP_OPTION_CHOICE_ENUM_UNSTABLE_SLEEP
        unstable_sleep_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.UNSTABLE_SLEEP_OPTION_TYPE,
            values = [
                (
                    "en", unstable_sleep_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        unstable_sleep_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.UNSTABLE_SLEEP_OPTION, 
            enum_type=unstable_sleep_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=sleep_root,
            child=unstable_sleep_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        #sleep quality
        sleep_quality_choices = [] + const.MDC_SLEEP_OPTION_CHOICE_ENUM_SLEEP_QUALITY
        sleep_quality_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.SLEEP_QUALITY_OPTION_TYPE,
            values = [
                (
                    "en", sleep_quality_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        sleep_quality_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.SLEEP_QUALITY_OPTION, 
            enum_type=sleep_quality_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=sleep_root,
            child=sleep_quality_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        #frequency take medicine to sleep per month
        sleep_medi_choices = [] + const.MDC_SLEEP_OPTION_CHOICE_ENUM_CANNOT_SLEEP
        sleep_medi_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.CANNOT_SLEEP_OPTION_TYPE,
            values = [
                (
                    "en", sleep_medi_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        sleep_medi_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.CANNOT_SLEEP_OPTION, 
            enum_type=sleep_medi_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=sleep_root,
            child=sleep_medi_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        #stay awake while doing social activities
        stay_awake_choices = [] + const.MDC_SLEEP_OPTION_CHOICE_ENUM_CANNOT_SLEEP
        stay_awake_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.CANNOT_SLEEP_OPTION_TYPE,
            values = [
                (
                    "en", stay_awake_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        stay_awake_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.CANNOT_SLEEP_OPTION, 
            enum_type=stay_awake_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=sleep_root,
            child=stay_awake_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        #problems to keep enthusiatic
        problems_choices = [] + const.MDC_SLEEP_OPTION_CHOICE_ENUM_PROBLEMS
        problems_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.PROBLEMS_OPTION_TYPE,
            values = [
                (
                    "en", problems_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        problems_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.PROBLEMS_OPTION, 
            enum_type=problems_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=sleep_root,
            child=problems_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        #snore loudly
        snore_loudly, _ = senses_models.BooleanObservationProfile.objects.get_or_create(
            name=const.SNORE_LOUDLY
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=sleep_root,
            child=snore_loudly,
            num_occurences=senses_const.ONE
        )

        #sleepy during daytime
        sleepy_daytime, _ = senses_models.BooleanObservationProfile.objects.get_or_create(
            name=const.SLEEPY_DAYTIME
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=sleep_root,
            child=sleepy_daytime,
            num_occurences=senses_const.ONE
        )

        #stop breathing during sleep
        stop_breath_inasleep, _ = senses_models.BooleanObservationProfile.objects.get_or_create(
            name=const.STOP_BREATH_INASLEEP
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=sleep_root,
            child=stop_breath_inasleep,
            num_occurences=senses_const.ONE
        )

        #is large shirt?
        is_large_shirt, _ = senses_models.BooleanObservationProfile.objects.get_or_create(
            name=const.IS_LARGE_SHIRT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=sleep_root,
            child=is_large_shirt,
            num_occurences=senses_const.ONE
        )

        senses_models.ObservationProfile.objects.activate(const.SLEEP_ROOT)

        self._add_frontends_to_profile(sleep_root)
        for profile in senses_models.ObservationProfile.objects.all():
            self._add_frontends_to_profile(profile)

    def baseline_health(self):
        root, _ = senses_models.ObservationProfile.objects.get_or_create_root_profile()

        #----baseline_health---
        health_root, _ = senses_models.ExtensibleRootObservationProfile.objects.get_or_create(
            name=const.HEALTH_ROOT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=root,
            child=health_root,
            num_occurences=senses_const.ZERO_OR_MORE
        )

        #diseases
        had_diseases_choices = [] + const.MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES
        had_diseases_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.HAD_DISEASES_OPTION_TYPE,
            values = [
                (
                    "en", had_diseases_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        had_diseases_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.HAD_DISEASES_OPTION, 
            enum_type=had_diseases_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=health_root,
            child=had_diseases_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        #has other illness
        has_other_illness, _ = senses_models.BooleanObservationProfile.objects.get_or_create(
            name=const.HAS_OTHER_ILLNESS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=health_root,
            child=has_other_illness,
            num_occurences=senses_const.ONE_OR_MORE
        )

        #WHAT ILLNESS
        illness, _ = senses_models.TextObservationProfile.objects.get_or_create(
            name=const.ILLNESS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=health_root,
            child=illness,
            num_occurences=senses_const.ONE_OR_MORE
        )
        senses_models.ObservationProfile.objects.activate(const.HEALTH_ROOT)

        self._add_frontends_to_profile(health_root)
        for profile in senses_models.ObservationProfile.objects.all():
            self._add_frontends_to_profile(profile)

    def baseline_wellbeing(self):
        root, _ = senses_models.ObservationProfile.objects.get_or_create_root_profile()

        #----baseline_wellbeing---
        wellbeing_root, _ = senses_models.ExtensibleRootObservationProfile.objects.get_or_create(
            name=const.WELLBEING_ROOT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=root,
            child=wellbeing_root,
            num_occurences=senses_const.ZERO_OR_MORE
        )

        #choices of frequency about diff feelings
        #nervous
        feeling_frequency_choices = [] + const.MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCY
        feeling_frequency_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.FEELING_FREQUENCY_OPTION_TYPE,
            values = [
                (
                    "en", feeling_frequency_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        nervous_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.NERVOUS_OPTION, 
            enum_type=feeling_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=nervous_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        #HOPELESS
        hopeless_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.HOPELESS_OPTION, 
            enum_type=feeling_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=hopeless_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        #RESTLESS OF FIDGETY
        restless_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.RESTLESS_OPTION, 
            enum_type=feeling_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=restless_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        #So depressed that nothing could cheer you up
        depressed_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.DEPRESSED_OPTION, 
            enum_type=feeling_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=depressed_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        #That everything was an effort
        exhausted_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.EXHUASTED_OPTION, 
            enum_type=feeling_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=exhausted_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        #Worthless
        worthless_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.WORTHLESS_OPTION, 
            enum_type=feeling_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=worthless_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        #bothering problems 1
        bothered_frequency_choices = [] + const.MDC_WELLBEING_OPTION_CHOICE_ENUM_BOTHERED_FREQUENCY
        bothered_frequency_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.BOTHERED_FREQUENCY_OPTION_TYPE,
            values = [
                (
                    "en", bothered_frequency_choices
                )
            ],
            use_internal_name_scheme=False,
        )

        #Feeling nervous, anxious, or on edge
        nae_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.NAE_OPTION, 
            enum_type=bothered_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=nae_option,
            num_occurences=senses_const.ONE
        )

        #Not being able to stop or control worrying.
        '''keep_worrying_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.KEEP_WORRYING_OPTION, 
            enum_type=bothered_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=keep_worrying_option,
            num_occurences=senses_const.ONE
        )

        #Worrying too much about different things.
        worrying_alot_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.WORRYING_ALOT_OPTION, 
            enum_type=bothered_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=worrying_alot_option,
            num_occurences=senses_const.ONE
        )

        #Trouble relaxing.
        trouble_relaxing_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.TROUBLE_RELAXING_OPTION, 
            enum_type=bothered_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=trouble_relaxing_option,
            num_occurences=senses_const.ONE
        )

        #Being so restless that it's hard to sit still.
        restless_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.RESTLESS_OPTION, 
            enum_type=bothered_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=restless_option,
            num_occurences=senses_const.ONE
        )

        #Becoming easily annoyed or irritable.
        easily_annoyed_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.EASILY_ANNOYED_OPTION, 
            enum_type=bothered_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=easily_annoyed_option,
            num_occurences=senses_const.ONE
        )

        #Feeling afraid as if something awful might happen.
        passive_thinking_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.PASSIVE_THINKING_OPTION, 
            enum_type=bothered_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=passive_thinking_option,
            num_occurences=senses_const.ONE
        )'''

        #If you checked off any problems, how difficult have these made it for you to do your work, take care of things at home, or get along with other people? 
        difficulty_choices = [] + const.MDC_WELLBEING_OPTION_CHOICE_ENUM_DIFFICULTY
        difficulty_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.DIFFICULTY_OPTION_TYPE,
            values = [
                (
                    "en", difficulty_choices
                )
            ],
            use_internal_name_scheme=False,
        )

        bothering_problems_1_difficulty_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.BOTHERING_PROBLEMS_1_DIFFICULTY_OPTION, 
            enum_type=difficulty_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=bothering_problems_1_difficulty_option,
            num_occurences=senses_const.ONE
        )

        #bothering problems 2
        #Little interest or pleasure in doing things.
        lil_pleasure_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.LIL_PLEASURE_OPTION, 
            enum_type=bothered_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=lil_pleasure_option,
            num_occurences=senses_const.ONE
        )

        #Feeling down, depressed, or hopeless.
        ddh_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.DDH_OPTION, 
            enum_type=bothered_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=ddh_option,
            num_occurences=senses_const.ONE
        )

        #Trouble falling or staying asleep, or sleeping too much.
        sleep_problem_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.SLEEP_PROBLEM_OPTION, 
            enum_type=bothered_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=sleep_problem_option,
            num_occurences=senses_const.ONE
        )

        #Feeling tired or having little energy.
        lil_energy_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.LIL_ENERGY_OPTION, 
            enum_type=bothered_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=lil_energy_option,
            num_occurences=senses_const.ONE
        )

        #Poor appetite or overeating.
        eat_problem_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.EAT_PROBLEM_OPTION, 
            enum_type=bothered_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=eat_problem_option,
            num_occurences=senses_const.ONE
        )

        #Feeling bad about yourself? or that you are a failure or have let yourself or your family down
        poor_self_judgement_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.POOR_SELF_JUDGEMENT_OPTION, 
            enum_type=bothered_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=poor_self_judgement_option,
            num_occurences=senses_const.ONE
        )

        #Trouble concentrating on things, such as reading the newspaper or watching television
        cannot_concentrate_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.CANNOT_CONCENTRATE_OPTION, 
            enum_type=bothered_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=cannot_concentrate_option,
            num_occurences=senses_const.ONE
        )

        #Moving or speaking so slowly that other people could have noticed. Or the opposite ?being so fidgety or restless that you have been moving around a lot more than usual.
        awkward_action_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.AWKWARD_ACTION_OPTION, 
            enum_type=bothered_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=awkward_action_option,
            num_occurences=senses_const.ONE
        )

        #Thoughts that you would be better off dead, or of hurting yourself in some way.
        suicide_thought_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.SUICIDE_THOUGHT_OPTION, 
            enum_type=bothered_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=suicide_thought_option,
            num_occurences=senses_const.ONE
        )

        #difficulty in life
        bothering_problems_2_difficulty_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.BOTHERING_PROBLEMS_2_DIFFICULTY_OPTION, 
            enum_type=difficulty_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=bothering_problems_2_difficulty_option,
            num_occurences=senses_const.ONE
        )


        #q4 spend with closest ppl
        hangout_time, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.HANGOUT_TIME
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=hangout_time,
            num_occurences=senses_const.ONE
        )

        #Talk to someone
        calling_time, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.CALLING_TIME
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=calling_time,
            num_occurences=senses_const.ONE
        )

        #MEETINGS TIME
        meetings_time, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.MEETINGS_TIME
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=meetings_time,
            num_occurences=senses_const.ONE
        )

        ## of ppl i can rely on living near me
        near_friends, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.NEAR_FRIENDS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=near_friends,
            num_occurences=senses_const.ONE
        )

        #q6 tbd
        #should I use text or choices
        occuring_frequency_choices = [] + const.MDC_WELLBEING_OPTION_CHOICE_ENUM_OCCURING_FREQUENCY
        occuring_frequency_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.OCCURING_FREQUENCY_OPTION_TYPE,
            values = [
                (
                    "en", occuring_frequency_choices
                )
            ],
            use_internal_name_scheme=False,
        )

        #Your partner makes you feel cared for
        cared_partner_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.CARED_PARTNER_OPTION, 
            enum_type=occuring_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=cared_partner_option,
            num_occurences=senses_const.ONE
        )

        #Your partner makes too many demands on you
        demanding_partner_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.DEMANDING_PARTNER_OPTION, 
            enum_type=occuring_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=demanding_partner_option,
            num_occurences=senses_const.ONE
        )

        #Other family members make you feel cared for
        cared_family_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.CARED_FAMILY_OPTION, 
            enum_type=occuring_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=cared_family_option,
            num_occurences=senses_const.ONE
        )
        
        #Other family members make too many demands on you
        demanding_family_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.DEMANDING_FAMILY_OPTION, 
            enum_type=occuring_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=demanding_family_option,
            num_occurences=senses_const.ONE
        )
        
        #Friends make too make demands on you 

        demanding_friends_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.DEMANDING_FRIENDS_OPTION, 
            enum_type=occuring_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=demanding_friends_option,
            num_occurences=senses_const.ONE
        )

        #same to q7
        #Co-workers make you feel cared for
        cared_co_workers_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.CARED_CO_WORKERS_OPTION, 
            enum_type=occuring_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=cared_co_workers_option,
            num_occurences=senses_const.ONE
        )
        #Co-workers make too many demands on you
        demanding_co_workers_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.DEMANDING_CO_WORKERS_OPTION, 
            enum_type=occuring_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=demanding_co_workers_option,
            num_occurences=senses_const.ONE
        )

        #Co-workers express interest in how you are doing
        interest_from_co_workers_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.INTEREST_FROM_CO_WORKERS_OPTION, 
            enum_type=occuring_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=interest_from_co_workers_option,
            num_occurences=senses_const.ONE
        )

        #Co-workers criticise you
        criticising_co_workers_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.CRITICISING_CO_WORKERS_OPTION, 
            enum_type=occuring_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=criticising_co_workers_option,
            num_occurences=senses_const.ONE
        )
        #Co-workers create tensions or have arguments with you
        conflict_with_co_workers_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.CONFLICT_WITH_CO_WORKERS_OPTION, 
            enum_type=occuring_frequency_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=conflict_with_co_workers_option,
            num_occurences=senses_const.ONE
        )



        #certain place for healthcare
        had_healthcare_place, _ = senses_models.BooleanObservationProfile.objects.get_or_create(
            name=const.HAD_HEALTHCARE_PLACE
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=had_healthcare_place,
            num_occurences=senses_const.ONE
        )

        #IT IS? CHOICES
        healthcare_place_choice = [] + const.MDC_WELLBEING_OPTION_CHOICE_ENUM_HEALTHCARE_PLACE
        healthcare_place_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.HEALTHCARE_PLACE_OPTION_TYPE,
            values = [
                (
                    "en", healthcare_place_choice
                )
            ],
            use_internal_name_scheme=False,
        )
        healthcare_place_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.HEALTHCARE_PLACE_OPTION, 
            enum_type=healthcare_place_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=healthcare_place_option,
            num_occurences=senses_const.ONE_OR_MORE
        )
        
        #healthcare situtation
        immediate_apointment, _ = senses_models.TextObservationProfile.objects.get_or_create(
            name=const.IMMEDIATE_APPOINTMENT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=immediate_apointment,
            num_occurences=senses_const.ONE
        )

        know_medi_history, _ = senses_models.TextObservationProfile.objects.get_or_create(
            name=const.KNOW_MEDI_HISTORY
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=know_medi_history,
            num_occurences=senses_const.ONE
        )

        coordination, _ = senses_models.TextObservationProfile.objects.get_or_create(
            name=const.COORDINATION
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=wellbeing_root,
            child=coordination,
            num_occurences=senses_const.ONE
        )

        senses_models.ObservationProfile.objects.activate(const.WELLBEING_ROOT)
        
        self._add_frontends_to_profile(wellbeing_root)
        for profile in senses_models.ObservationProfile.objects.all():
            self._add_frontends_to_profile(profile)


    def daily_wellbeing(self):
        #Anxiety and depression
        root, _ = senses_models.ObservationProfile.objects.get_or_create_root_profile()
        
        daily_wellbeing_root, _ = senses_models.ExtensibleRootObservationProfile.objects.get_or_create(
            name=const.DAILY_WELLBEING_ROOT
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=root, child=daily_wellbeing_root, num_occurences=senses_const.ZERO_OR_MORE
        )

        #anxiety and depression

        #Over the last 24 hours how often have you been bothered by the following:
        feeling_frequencies_choice = [] + const.MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCIES
        feeling_frequencies_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.FEELING_FREQUENCIES_OPTION_TYPE,
            values = [
                (
                    "en", feeling_frequencies_choice
                )
            ],
            use_internal_name_scheme=False,
        )

        #feeling nervous, anxious or on edge
        daily_nae_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.DAILY_NAE_OPTION, 
            enum_type=feeling_frequencies_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_wellbeing_root,
            child=daily_nae_option,
            num_occurences=senses_const.ONE
        )

        #Not being able to stop or control worrying
        daily_keep_worrying_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.DAILY_KEEP_WORRYING_OPTION, 
            enum_type=feeling_frequencies_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_wellbeing_root,
            child=daily_keep_worrying_option,
            num_occurences=senses_const.ONE
        )

        #Feeling down, depressed, or hopeless
        daily_ddh_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.DAILY_DDH_OPTION, 
            enum_type=feeling_frequencies_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_wellbeing_root,
            child=daily_ddh_option,
            num_occurences=senses_const.ONE
        )

        #Little interest or pleasure in doing things
        daily_lil_pleasure_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.DAILY_LIL_PLEASURE_OPTION, 
            enum_type=feeling_frequencies_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_wellbeing_root,
            child=daily_lil_pleasure_option,
            num_occurences=senses_const.ONE
        )

        #How are you feeling right now? [0-10, unhappy to happy] 
        feeling_rn, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.FEELING_RN
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_wellbeing_root,
            child=feeling_rn,
            num_occurences=senses_const.ONE
        )

        #How satisfied are you with your life at this moment? [0-10, unsatisfied to satisfied]
        satisfaction, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.SATISFACTION
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_wellbeing_root,
            child=satisfaction,
            num_occurences=senses_const.ONE
        )

        #Pain
        #physical pain [0-6] optional
        physical_pain, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.PHYSICAL_PAIN
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_wellbeing_root,
            child=physical_pain,
            num_occurences=senses_const.ONE
        )

        #Please rate your pain by selecting the one number that best describes your pain on the average [ scale from 0 to 10; 0="no pain", 5="moderate pain" 10="worst pain imaginable"
        physical_pain_lvl, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.PHYSICAL_PAIN_LVL
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_wellbeing_root,
            child=physical_pain_lvl,
            num_occurences=senses_const.ZERO_OR_ONE
        )

        self._add_frontends_to_profile(daily_wellbeing_root)
        for profile in senses_models.ObservationProfile.objects.all():
            self._add_frontends_to_profile(profile)

        
    def daily_diet(self):
        root, _ = senses_models.ObservationProfile.objects.get_or_create_root_profile()
        
        daily_diet_root, _ = senses_models.ExtensibleRootObservationProfile.objects.get_or_create(
            name=const.DAILY_DIET_ROOT
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=root, child=daily_diet_root, num_occurences=senses_const.ZERO_OR_MORE
        )

        #Fruit
        #serves of fruit
        daily_serves_of_fruit, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.DAILY_SERVES_OF_FRUIT
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_diet_root,
            child=daily_serves_of_fruit,
            num_occurences=senses_const.ONE
        )

        #serves of vegetables
        daily_serves_of_vege, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.DAILY_SERVES_OF_VEGE
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_diet_root,
            child=daily_serves_of_vege,
            num_occurences=senses_const.ONE
        )

        #drinks
        #[0-10] cups (250mL) of Soft drink, cordials or sports drink, such as lemonade or Gatorade, with sugar
        daily_cups_of_soft_drinks, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.DAILY_CUPS_OF_SOFT_DRINKS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_diet_root,
            child=daily_cups_of_soft_drinks,
            num_occurences=senses_const.ONE
        )

        #[0-10] cups (250mL) of tea, coffee, soft drinks, sports drinks or energy drinks that contain caffeine Cans normally contain 330 mL.
        daily_cups_of_caffeine_drinks, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.DAILY_CUPS_OF_CAFFEINE_DRINKS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_diet_root,
            child=daily_cups_of_caffeine_drinks,
            num_occurences=senses_const.ONE
        )

        #Discretionary foods
        #Today I have eaten [ ] meals of burgers, pizza, chicken or chips from places like McDonalds, Hungry Jacks, Pizza Hut, KFC, Red Rooster, or local take-away places
        daily_meals_of_burgers, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.DAILY_MEALS_OF_BURGERS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_diet_root,
            child=daily_meals_of_burgers,
            num_occurences=senses_const.ONE
        )

        #Today I have eaten [ ] serves of hot chips, French fries, wedges or fried potatoes
        daily_serves_of_fries, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.DAILY_SERVES_OF_FRIES
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_diet_root,
            child=daily_serves_of_fries,
            num_occurences=senses_const.ONE
        )

        #Today I have eaten [ ] serves of potato crisps, savoury biscuits or other salty snacks such as twisties or corn chips
        daily_serves_of_salty_snacks, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.DAILY_SERVES_OF_SALTY_SNACKS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_diet_root,
            child=daily_serves_of_salty_snacks,
            num_occurences=senses_const.ONE
        )

        #Today I have eaten [ ] serves of sweet biscuits, cakes, pastries, or snack bars
        daily_serves_of_sweet_snacks, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.DAILY_SERVES_OF_SWEET_SNACKS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_diet_root,
            child=daily_serves_of_sweet_snacks,
            num_occurences=senses_const.ONE
        )

        #Today I have eaten [ ] serves of confectionary (chocolate, confectionary bars and lollies, or ice cream)
        daily_serves_of_confectionary, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.DAILY_SERVES_OF_CONFECTIONARY
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_diet_root,
            child=daily_serves_of_confectionary,
            num_occurences=senses_const.ONE
        )       

        self._add_frontends_to_profile(daily_diet_root)
        for profile in senses_models.ObservationProfile.objects.all():
            self._add_frontends_to_profile(profile) 
        
    def daily_alcohol_smoking(self):
        #Alcohol and Smoking will only be offered if the user indicates they currently use these substances in the baseline survey.
        root, _ = senses_models.ObservationProfile.objects.get_or_create_root_profile()
        
        daily_alcohol_smoking_root, _ = senses_models.ExtensibleRootObservationProfile.objects.get_or_create(
            name=const.DAILY_ALCOHOL_SMOKING_ROOT
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=root, child=daily_alcohol_smoking_root, num_occurences=senses_const.ZERO_OR_MORE
        )
        
        #Alcoholic drinks
        daily_standard_alcoholic_drinks, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.DAILY_STANDARD_ALCOHOLIC_DRINKS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_alcohol_smoking_root,
            child=daily_standard_alcoholic_drinks,
            num_occurences=senses_const.ZERO_OR_MORE
        )

        #cigarettes
        #Today I have smoked [number] [cigarettes/packs of cigarettes]
        daily_cigarettes, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.DAILY_CIGARETTES
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_alcohol_smoking_root,
            child=daily_cigarettes,
            num_occurences=senses_const.ZERO_OR_MORE
        )

        self._add_frontends_to_profile(daily_alcohol_smoking_root)
        for profile in senses_models.ObservationProfile.objects.all():
            self._add_frontends_to_profile(profile) 


    
    #Input of physical activity and sleep is dependent on availability of wearable devices and level of data integration with the Healthy Heads app (as detailed in report).
    #For physical activity and alcohol consumption daily data will also be integrated into a weekly value to allow assessment against current weekly guidelines
    def daily_physical_activity(self):
        root, _ = senses_models.ObservationProfile.objects.get_or_create_root_profile()
        
        daily_physical_activity_root, _ = senses_models.ExtensibleRootObservationProfile.objects.get_or_create(
            name=const.DAILY_PHYSICAL_ACTIVITY_ROOT
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=root, child=daily_physical_activity_root, num_occurences=senses_const.ZERO_OR_MORE
        )

        #wearable device
        minutes, _ = senses_models.MeasurementUnit.objects.get_or_create(
            name=const.MDC_DAILY_MINS
        )
        hours_unit, _ = senses_models.MeasurementUnit.objects.get_or_create(
            name=const.MDC_DAILY_HOURS
        )

        daily_vigorous_activity, _ = senses_models.SensorReadingObservationProfile.objects.get_or_create(
            name=const.DAILY_VIGOROUS_ACTIVITY, unit=minutes
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_physical_activity_root, child=daily_vigorous_activity, num_occurences=senses_const.ZERO_OR_MORE
        )

        #moderate
        daily_moderate_activity, _ = senses_models.SensorReadingObservationProfile.objects.get_or_create(
            name=const.DAILY_MODERATE_ACTIVITY, unit=minutes
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_physical_activity_root, child=daily_moderate_activity, num_occurences=senses_const.ZERO_OR_MORE
        )

        #sedentary
        daily_sedentary_activity, _ = senses_models.SensorReadingObservationProfile.objects.get_or_create(
            name=const.DAILY_SEDENTARY_ACTIVITY, unit=hours_unit
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_physical_activity_root, child=daily_sedentary_activity, num_occurences=senses_const.ZERO_OR_MORE
        )

        self._add_frontends_to_profile(daily_physical_activity_root)
        for profile in senses_models.ObservationProfile.objects.all():
            self._add_frontends_to_profile(profile) 
    
    
    def daily_sleep(self):
        #wearable device or user input?
        root, _ = senses_models.ObservationProfile.objects.get_or_create_root_profile()
        
        daily_sleep_root, _ = senses_models.ExtensibleRootObservationProfile.objects.get_or_create(
            name=const.DAILY_SLEEP_ROOT
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=root, child=daily_sleep_root, num_occurences=senses_const.ZERO_OR_MORE
        )

        #wearable device
        #am/pm
        am_pm, _ = senses_models.MeasurementUnit.objects.get_or_create(
            name=const.MDC_DAILY_TIME
        )

        #bed time
        daily_bed_time, _ = senses_models.SensorReadingObservationProfile.objects.get_or_create(
            name=const.DAILY_BED_TIME, unit=am_pm
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_sleep_root, child=daily_bed_time, num_occurences=senses_const.ZERO_OR_MORE
        )

        #asleep time
        daily_asleep_time, _ = senses_models.SensorReadingObservationProfile.objects.get_or_create(
            name=const.DAILY_ASLEEP_TIME, unit=am_pm
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_sleep_root, child=daily_asleep_time, num_occurences=senses_const.ZERO_OR_MORE
        )

        #wakeup time
        daily_wakeup_time, _ = senses_models.SensorReadingObservationProfile.objects.get_or_create(
            name=const.DAILY_WAKEUP_TIME, unit=am_pm
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_sleep_root, child=daily_wakeup_time, num_occurences=senses_const.ZERO_OR_MORE
        )

        #whether used alarmed
        alarm_used, _ = senses_models.BooleanObservationProfile.objects.get_or_create(
            name=const.ALARM_USED
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_sleep_root,
            child=alarm_used,
            num_occurences=senses_const.ONE
        )

        #sleep quality
        #0-4
        daily_sleep_quality, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.DAILY_SLEEP_QUALITY
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_sleep_root, child=daily_sleep_quality, num_occurences=senses_const.ZERO_OR_MORE
        )

        self._add_frontends_to_profile(daily_sleep_root)
        for profile in senses_models.ObservationProfile.objects.all():
            self._add_frontends_to_profile(profile) 
    
    
    def daily_work(self):
        root, _ = senses_models.ObservationProfile.objects.get_or_create_root_profile()
        
        daily_work_root, _ = senses_models.ExtensibleRootObservationProfile.objects.get_or_create(
            name=const.DAILY_WORK_ROOT
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=root, child=daily_work_root, num_occurences=senses_const.ZERO_OR_MORE
        )

        #work day or not
        is_work_day, _ = senses_models.BooleanObservationProfile.objects.get_or_create(
            name=const.IS_WORK_DAY
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_work_root,
            child=is_work_day,
            num_occurences=senses_const.ONE
        )

        #number of hours of work [1-24] hours
        daily_work_hours, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.DAILY_WORK_HOURS
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_work_root,
            child=daily_work_hours,
            num_occurences=senses_const.ZERO_OR_MORE
        )

        #I am working [during the day/during the night]
        shift_time_choices = [] + const.MDC_DAILY_WORK_OPTION_CHOICE_ENUM_SHIFT_TIME
        shift_time_option_enum, _ = senses_models.EnumerationType.objects.get_or_create_from_list(
            name = const.SHIFT_TIME_OPTION_TYPE,
            values = [
                (
                    "en", shift_time_choices
                )
            ],
            use_internal_name_scheme=False,
        )
        shift_time_option, _ = senses_models.EnumerationObservationProfile.objects.get_or_create(
            name = const.SHIFT_TIME_OPTION, enum_type=shift_time_option_enum
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=daily_work_root,
            child=shift_time_option,
            num_occurences=senses_const.ONE_OR_MORE
        )

        self._add_frontends_to_profile(daily_work_root)
        for profile in senses_models.ObservationProfile.objects.all():
            self._add_frontends_to_profile(profile)


    def healthscore(self):
        #store the calculated health score data from app side
        # Each of the 5 domains will contribute 20 points to produce a score out of 100 with best health indicated by a score of 100. 
        # i) mental health and wellbeing, ii) diet, iii) alcohol and smoking, iv) physical activity/sedentary behaviour and v)sleep. 
        root, _ = senses_models.ObservationProfile.objects.get_or_create_root_profile()
        
        healthscore_root, _ = senses_models.ExtensibleRootObservationProfile.objects.get_or_create(
            name=const.HEALTSCORE_ROOT
        )

        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=root, child=healthscore_root, num_occurences=senses_const.ZERO_OR_MORE
        )

        #mental health and wellbeing 0-20
        wellbeing_score, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.WELLBEING_SCORE
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=healthscore_root,
            child=wellbeing_score,
            num_occurences=senses_const.ONE
        )

        #diet 0-20
        diet_score, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.DIET_SCORE
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=healthscore_root,
            child=diet_score,
            num_occurences=senses_const.ONE
        )

        #alcohol and smoking 0-20
        alcohol_smoking_score, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.ALCOHOL_SMOKING_SCORE
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=healthscore_root,
            child=alcohol_smoking_score,
            num_occurences=senses_const.ONE
        )

        #physical activity/sedentary behaviour 0-20
        pa_score, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.PA_SCORE
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=healthscore_root,
            child=pa_score,
            num_occurences=senses_const.ONE
        )

        #sleep 0-20
        sleep_score, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.SLEEP_SCORE
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=healthscore_root,
            child=sleep_score,
            num_occurences=senses_const.ONE
        )

        #final health score
        final_score, _ = senses_models.NumericObservationProfile.objects.get_or_create(
            name=const.FINAL_HEALTHSCORE
        )
        senses_models.RelatedObservationProfile.objects.get_or_create(
            parent=healthscore_root,
            child=final_score,
            num_occurences=senses_const.ONE
        )

        self._add_frontends_to_profile(healthscore_root)
        for profile in senses_models.ObservationProfile.objects.all():
            self._add_frontends_to_profile(profile) 

    def _add_frontends_to_profile(self, profile):
        # add frontends by default: webinterface and mobilemonitor (and api, already set)
        web = senses_models.Frontend.objects.get(name=senses_const.FRONTEND__WEBFRONTEND)
        api = senses_models.Frontend.objects.get(name=senses_const.FRONTEND__API)
        mm = senses_models.Frontend.objects.get(name=cares_const.FRONTEND__MOBILE_MONITOR)
        cwd = senses_models.Frontend.objects.get(name=cares_const.FRONTEND__CARES_WEB_DEVICE)

        profile.frontends.add(web)
        profile.frontends.add(api)
        profile.frontends.add(mm)
        profile.frontends.add(cwd)