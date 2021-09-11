from kiola.cares import const as cares_const
from kiola.kiola_senses import const as senses_const

#root for demographics
DEMO_ROOT = "MDC_DEV_SPEC_PROFILE_STU_BASELINE_DEMO"

MDC_DEMO_OCCUPATION_OPTION = "MDC_DEMO_OCCUPATION_OPTION_CHOICE"
MDC_DEMO_OCCUPATION_OPTION_TYPE = "MDC_DEMO_OCCUPATION_OPTION_CHOICE_ENUM_TYPE"


MDC_DEMO_OPTION_CHOICE_ENUM_OCCUPATION_0 = "truck_driver"
MDC_DEMO_OPTION_CHOICE_ENUM_OCCUPATION_1 = "desk_based_role"
MDC_DEMO_OPTION_CHOICE_ENUM_OCCUPATION_2 = "physically_active_warehouse_role"
MDC_DEMO_OPTION_CHOICE_ENUM_OCCUPATION = [
  MDC_DEMO_OPTION_CHOICE_ENUM_OCCUPATION_0,
  MDC_DEMO_OPTION_CHOICE_ENUM_OCCUPATION_1,
  MDC_DEMO_OPTION_CHOICE_ENUM_OCCUPATION_2,
]

WORKING_DAYS = "MDC_STU_WORKING_DAYS"
SHIFTED_WORK = "MDC_VND_AIT_MODE_SHIFTED_WORK"


SHIFT_TYPE_OPTION = "MDC_DEMO_SHIFT_TYPE_OPTION_CHOICE"
SHIFT_TYPE_OPTION_TYPE = "MDC_DEMO_SHIFT_TYPE_OPTION_CHOICE_ENUM_TYPE"
MDC_DEMO_OPTION_CHOICE_ENUM_SHIFT_TYPE_0 = "rotating_shift_with_periodic_change"
MDC_DEMO_OPTION_CHOICE_ENUM_SHIFT_TYPE_1 = "regular_overnight_or_graveyard_shift"
MDC_DEMO_OPTION_CHOICE_ENUM_SHIFT_TYPE_2= "regular_afternoon_or_evening_shift"
MDC_DEMO_OPTION_CHOICE_ENUM_SHIFT_TYPE_3 = "regular_morning_shift"
MDC_DEMO_OPTION_CHOICE_ENUM_SHIFT_TYPE_4 = "irregular_shift"
MDC_DEMO_OPTION_CHOICE_ENUM_SHIFT_TYPE_5 = "split_shift_consisting_of_two_distinct_periods_each_day_or_oncall"
MDC_DEMO_OPTION_CHOICE_ENUM_SHIFT_TYPE_6 = "other"
MDC_DEMO_OPTION_CHOICE_ENUM_SHIFT_TYPE = [
    MDC_DEMO_OPTION_CHOICE_ENUM_SHIFT_TYPE_0,
    MDC_DEMO_OPTION_CHOICE_ENUM_SHIFT_TYPE_1,
    MDC_DEMO_OPTION_CHOICE_ENUM_SHIFT_TYPE_2,
    MDC_DEMO_OPTION_CHOICE_ENUM_SHIFT_TYPE_3,
    MDC_DEMO_OPTION_CHOICE_ENUM_SHIFT_TYPE_4,
    MDC_DEMO_OPTION_CHOICE_ENUM_SHIFT_TYPE_5,
    MDC_DEMO_OPTION_CHOICE_ENUM_SHIFT_TYPE_6,
]

AGE = "MDC_STU_AGE"

GENDER_OPTION = "MDC_DEMO_GENDER_OPTION_CHOICE"
GENDER_OPTION_TYPE = "MDC_DEMO_GENDER_OPTION_CHOICE_ENUM_TYPE"
MDC_DEMO_OPTION_CHOICE_ENUM_GENDER_0 = "male"
MDC_DEMO_OPTION_CHOICE_ENUM_GENDER_1 = "female"
MDC_DEMO_OPTION_CHOICE_ENUM_GENDER_2 = "other"
MDC_DEMO_OPTION_CHOICE_ENUM_GENDER_3 = "prefer_not_to_say"
MDC_DEMO_OPTION_CHOICE_ENUM_GENDER = [
    MDC_DEMO_OPTION_CHOICE_ENUM_GENDER_0,
    MDC_DEMO_OPTION_CHOICE_ENUM_GENDER_1,
    MDC_DEMO_OPTION_CHOICE_ENUM_GENDER_2,
    MDC_DEMO_OPTION_CHOICE_ENUM_GENDER_3,
] 

HEIGHT = "MDC_STU_HEIGHT"

WEIGHT = "MDC_STU_WEIGHT"

# --- smoking ----
#root for smoking
SMOKING_ROOT = "MDC_DEV_SPEC_PROFILE_STU_BASELINE_SMOKING"

SMOKING_STATUS_OPTION = "MDC_DEMO_SMOKING_STATUS_OPTION_CHOICE"
SMOKING_STATUS_OPTION_TYPE = "MDC_DEMO_SMOKING_STATUS_OPTION_CHOICE_ENUM_TYPE"
MDC_SMOKING_OPTION_CHOICE_ENUM_SMOKING_STATUS_0 = "Smoke_daily"
MDC_SMOKING_OPTION_CHOICE_ENUM_SMOKING_STATUS_1 = "Smoke_occasionally"
MDC_SMOKING_OPTION_CHOICE_ENUM_SMOKING_STATUS_2 = "Don_t_smoke_now_but_used_to_Approximate_date_stopped_smoking"
MDC_SMOKING_OPTION_CHOICE_ENUM_SMOKING_STATUS_3 = "Tried_it_a_few_times_but_never_smoked_regularly"
MDC_SMOKING_OPTION_CHOICE_ENUM_SMOKING_STATUS_4 = "Never_smoked_if_answered_5_then_skip_next_questions"
MDC_SMOKING_OPTION_CHOICE_ENUM_SMOKING_STATUS = [
    MDC_SMOKING_OPTION_CHOICE_ENUM_SMOKING_STATUS_0,
    MDC_SMOKING_OPTION_CHOICE_ENUM_SMOKING_STATUS_1,
    MDC_SMOKING_OPTION_CHOICE_ENUM_SMOKING_STATUS_2,
    MDC_SMOKING_OPTION_CHOICE_ENUM_SMOKING_STATUS_3,
    MDC_SMOKING_OPTION_CHOICE_ENUM_SMOKING_STATUS_4,
] 

MDC_ATTR_DATE_STOPPED_SMOKING = "MDC_ATTR_DATE_STOPPED_SMOKING"

CIGS_PER_DAY_OPTION = "MDC_DEMO_CIG_PER_DAY_OPTION_CHOICE"
CIGS_PER_DAY_OPTION_TYPE = "MDC_DEMO_CIGS_PER_DAY_OPTION_CHOICE_ENUM_TYPE"
MDC_SMOKING_OPTION_CHOICE_ENUM_CIGS_PER_DAY_0 = "1_to_10_cigarettes_per_day"
MDC_SMOKING_OPTION_CHOICE_ENUM_CIGS_PER_DAY_1 = "11_to_20_cigarettes_per_day_or"
MDC_SMOKING_OPTION_CHOICE_ENUM_CIGS_PER_DAY_2 = "21_or_more_cigarettes_per_day"
MDC_SMOKING_OPTION_CHOICE_ENUM_CIGS_PER_DAY_3 = "None_Exclusively_use_pipes_or_smoke_cigars"
MDC_SMOKING_OPTION_CHOICE_ENUM_CIGS_PER_DAY = [
    MDC_SMOKING_OPTION_CHOICE_ENUM_CIGS_PER_DAY_0,
    MDC_SMOKING_OPTION_CHOICE_ENUM_CIGS_PER_DAY_1,
    MDC_SMOKING_OPTION_CHOICE_ENUM_CIGS_PER_DAY_2,
    MDC_SMOKING_OPTION_CHOICE_ENUM_CIGS_PER_DAY_3,
]

FREQUENCY_OPTION = "MDC_DEMO_CIG_PER_DAY_OPTION_CHOICE"
FREQUENCY_OPTION_TYPE = "MDC_DEMO_CIGS_PER_DAY_OPTION_CHOICE_ENUM_TYPE"
MDC_SMOKING_OPTION_CHOICE_ENUM_FREQUENCY_0 = "Never_used_electronic_cigarettes"
MDC_SMOKING_OPTION_CHOICE_ENUM_FREQUENCY_1 = "Tried_electronic_cigarettes_a_few_times_but_never_used_them_regularly"
MDC_SMOKING_OPTION_CHOICE_ENUM_FREQUENCY_2 = "Don_t_use_electronic_cigarettes_now_but_used_to"
MDC_SMOKING_OPTION_CHOICE_ENUM_FREQUENCY_3 = "Use_electronic_cigarettes_occasionally"
MDC_SMOKING_OPTION_CHOICE_ENUM_FREQUENCY_3 = "Use_electronic_cigarettes_daily"
MDC_SMOKING_OPTION_CHOICE_ENUM_FREQUENCY = [
    MDC_SMOKING_OPTION_CHOICE_ENUM_FREQUENCY_0,
    MDC_SMOKING_OPTION_CHOICE_ENUM_FREQUENCY_1,
    MDC_SMOKING_OPTION_CHOICE_ENUM_FREQUENCY_2,
    MDC_SMOKING_OPTION_CHOICE_ENUM_FREQUENCY_3,
]

ALCOHOL_ROOT = "MDC_DEV_SPEC_PROFILE_STU_BASELINE_ALCOHOL"

DRINK_DAYS_OPTION = "MDC_DEMO_DRINK_DAYS_OPTION_CHOICE"
DRINK_DAYS_OPTION_TYPE = "MDC_DEMO_DRINK_DAYS_OPTION_CHOICE_ENUM_TYPE"
MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_0 = "7_days_per_wk"
MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_1 = "6_days_per_wk"
MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_2 = "5_days_per_wk"
MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_3 = "4_days_per_wk"
MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_4 = "3_days_per_wk"
MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_5 = "2_days_per_wk"
MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_6 = "1_day_per_wk"
MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_7 = "less_than_once_per_week"
MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_8 = "No_longer_drink_alcohol_Approximate_date_stopped_drinking_alcohol"
MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_9 = "I_don_t_drink_alcohol__skip_next_question"
MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_10 = "don_t_know"
MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_11 = "prefer_not_to_answer"
MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS = [
    MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_0,
    MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_1,
    MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_2,
    MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_3,
    MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_4,
    MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_5,
    MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_6,
    MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_7,
    MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_8,
    MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_9,
    MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_10,
    MDC_ALCOHOL_OPTION_CHOICE_ENUM_DRINK_DAYS_11,
]

MDC_ATTR_DATE_STOPPED_ALCOHOL = "MDC_ATTR_DATE_STOPPED_ALCOHOL"

STANDARD_OPTION = "MDC_DEMO_STANDARD_OPTION_CHOICE"
STANDARD_OPTION_TYPE = "MDC_DEMO_STANDARD_OPTION_CHOICE_ENUM_TYPE"
MDC_ALCOHOL_OPTION_CHOICE_ENUM_STANDARD_0 = "drinks"
MDC_ALCOHOL_OPTION_CHOICE_ENUM_STANDARD_1 = "Don_t_know"
MDC_ALCOHOL_OPTION_CHOICE_ENUM_STANDARD_2 = "Prefer_not_to_answer"
MDC_ALCOHOL_OPTION_CHOICE_ENUM_STANDARD = [
    MDC_ALCOHOL_OPTION_CHOICE_ENUM_STANDARD_0,
    MDC_ALCOHOL_OPTION_CHOICE_ENUM_STANDARD_1,
    MDC_ALCOHOL_OPTION_CHOICE_ENUM_STANDARD_2,
]

NUM_DRINKS = "MDC_STU_NUM_DRINKS"

#----diet---

DIET_ROOT = "MDC_DEV_SPEC_PROFILE_STU_BASELINE_DIET"

NEVER_EAT_OPTION = "MDC_DEMO_NEVER_EAT_OPTION_CHOICE"
NEVER_EAT_OPTION_TYPE = "MDC_DEMO_NEVER_EAT_OPTION_CHOICE_ENUM_TYPE"
MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_0 = "Any_meat"
MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_1 = "Red_meat"
MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_2 = "Pork_or_ham"
MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_3 = "Dairy_products"
MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_4 = "Cheese"
MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_5 = "Cream"
MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_6 = "Wheat_products"
MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_7 = "Fish"
MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_8 = "Chicken_or_poultry"
MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_9 = "Eggs"
MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_10 = "Seafood"
MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_11 = "Sugar"
MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_12 = "Vegetables"
MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_13 = "Fruit"

MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT = [
    MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_0,
    MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_1,
    MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_2,
    MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_3,
    MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_4,
    MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_5,
    MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_6,
    MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_7,
    MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_8,
    MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_9,
    MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_10,
    MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_11,
    MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_12,
    MDC_DIET_OPTION_CHOICE_ENUM_NEVER_EAT_13,
]

SERVES_OF_COOKED_VEGES = "MDC_STU_SERVES_OF_COOKED_VEGES"

SERVES_OF_RAW_VEGES = "MDC_STU_SERVES_OF_RAW_VEGES"

SERVES_OF_FRUIT = "MDC_STU_SERVES_OF_FRUIT"

SERVES_OF_FRUIT_JUICE = "MDC_STU_SERVES_OF_FRUIT_JUICE"

TIMES_EAT_BLP = "MDC_STU_TIMES_EAT_BLP"

TIMES_EAT_CTD = "MDC_STU_TIMES_EAT_CTD"

TIMES_EAT_PROC_MEAT = "MDC_STU_TIMES_EAT_PROC_MEAT"

TIMES_EAT_FISH_SEAFOOD = "MDC_STU_TIMES_EAT_FISH_SEAFOOD"

TIMES_EAT_CHEESE= "MDC_STU_TIMES_EAT_CHEESE"

BROWN_BREAD = "MDC_STU_BROWN_BREAD"

BREKKY_CEREAL = "MDC_STU_BREKKY_CEREAL"

BREKKY_CEREAL_OPTION = "MDC_DEMO_BREKKY_CEREAL_OPTION_CHOICE"
BREKKY_CEREAL_OPTION_TYPE = "MDC_DEMO_BREKKY_CEREAL_OPTION_CHOICE_ENUM_TYPE"
MDC_DIET_OPTION_CHOICE_ENUM_BREKKY_CEREAL_0 = "Bran_cereal"
MDC_DIET_OPTION_CHOICE_ENUM_BREKKY_CEREAL_1 = "Biscuit_cereal"
MDC_DIET_OPTION_CHOICE_ENUM_BREKKY_CEREAL_2 = "Oat_cereal"
MDC_DIET_OPTION_CHOICE_ENUM_BREKKY_CEREAL_3 = "Muesli"
MDC_DIET_OPTION_CHOICE_ENUM_BREKKY_CEREAL_4 = "Other"
MDC_DIET_OPTION_CHOICE_ENUM_BREKKY_CEREAL = [
    MDC_DIET_OPTION_CHOICE_ENUM_BREKKY_CEREAL_0,
    MDC_DIET_OPTION_CHOICE_ENUM_BREKKY_CEREAL_1,
    MDC_DIET_OPTION_CHOICE_ENUM_BREKKY_CEREAL_2,
    MDC_DIET_OPTION_CHOICE_ENUM_BREKKY_CEREAL_3,
    MDC_DIET_OPTION_CHOICE_ENUM_BREKKY_CEREAL_4,
]

MILK_OPTION = "MDC_DEMO_MILK_OPTION_CHOICE"
MILK_OPTION_TYPE = "MDC_DEMO_MILK_OPTION_CHOICE_ENUM_TYPE"
MDC_DIET_OPTION_CHOICE_ENUM_MILK_0 = "Whole_milk"
MDC_DIET_OPTION_CHOICE_ENUM_MILK_1 = "Soy_milk"
MDC_DIET_OPTION_CHOICE_ENUM_MILK_2 = "Reduced_fat_milk"
MDC_DIET_OPTION_CHOICE_ENUM_MILK_3 = "Other_milk"
MDC_DIET_OPTION_CHOICE_ENUM_MILK_4 = "Skim_milk"
MDC_DIET_OPTION_CHOICE_ENUM_MILK_5 = "I_don_t_drink_milk"
MDC_DIET_OPTION_CHOICE_ENUM_MILK = [
    MDC_DIET_OPTION_CHOICE_ENUM_MILK_0,
    MDC_DIET_OPTION_CHOICE_ENUM_MILK_1,
    MDC_DIET_OPTION_CHOICE_ENUM_MILK_2,
    MDC_DIET_OPTION_CHOICE_ENUM_MILK_3,
    MDC_DIET_OPTION_CHOICE_ENUM_MILK_4,
    MDC_DIET_OPTION_CHOICE_ENUM_MILK_5,
]

DRINKS_WITH_SUGAR = "MDC_STU_DRINKS_WITH_SUGAR"

DRINKS_WITHOUT_SUGAR = "MDC_STU_DRINKS_WITHOUT_SUGAR"

CAFFEINE_DRINKS = "MDC_STU_CAFFEINE_DRINKS"

FAST_FOOD_MEALS = "MDC_STU_FAST_FOOD_MEALS"

FRIED_FOOD = "MDC_STU_FRIED_FOOD"

TWISTIES_CHIPS = "MDC_STU_TWISTIES_CHIPS"

SWEET_SNACKS = "MDC_STU_SWEET_SNACKS"

CONFECTIONARY = "MDC_STU_CONFECTIONARY"


# --- PHYSICAL ACTIVITY ---
PHYSICAL_ACTIVITY_ROOT = "MDC_DEV_SPEC_PROFILE_STU_BASELINE_PHYSICAL_ACTIVITY"

INTENSE_WORK = "MDC_VND_AIT_MODE_INTENSE_WORK"

WORK_FREQUENCY = "MDC_STU_WORK_FREQUENCY"

MDC_ATTR_TIME_SPENT = "MDC_STU_TIME_SPENT"

BICYCLE_TRANSPORT = "MDC_VND_AIT_MODE_BICYCLE_TRANSPORT"

DAYS_TRANSPORT = "MDC_STU_DAYS_TRANSPORT"

MDC_ATTR_TIME_TRANSPORT = "MDC_ATTR_TIME_TRANSPORT"

DO_EXERCISE = "MDC_VND_AIT_MODE_DO_EXERCISE"

DAYS_EXERCISE = "MDC_STU_DAYS_EXERCISE"

MDC_ATTR_TIME_EXERCISE = "MDC_ATTR_TIME_EXERCISE"

MDC_ATTR_TIME_SITTING_RECLINING = "MDC_ATTR_TIME_SITTING_RECLINING"


# --- sleep ----
SLEEP_ROOT = "MDC_DEV_SPEC_PROFILE_STU_BASELINE_SLEEP_ROOT"

MDC_ATTR_WORK_BED_TIME = "MDC_ATTR_WORK_BED_TIME"

WORK_MIN_FALL_ASLEEP = "MDC_STU_WORK_MIN_FALL_ASLEEP"

MDC_ATTR_WORK_GET_UP_TIME = "MDC_ATTR_WORK_GET_UP_TIME"

WORK_SLEEPING_HOURS = "MDC_STU_WORK_SLEEPING_HOURS"

MDC_ATTR_FREE_BED_TIME = "MDC_ATTR_FREE_BED_TIME"

FREE_MIN_FALL_ASLEEP = "MDC_STU_FREE_MIN_FALL_ASLEEP"

MDC_ATTR_FREE_GET_UP_TIME = "MDC_ATTR_FREE_GET_UP_TIME"

FREE_SLEEPING_HOURS = "MDC_STU_FREE_SLEEPING_HOURS"

CANNOT_SLEEP_OPTION = "MDC_CANNOT_SLEEP_OPTION_CHOICE"
CANNOT_SLEEP_OPTION_TYPE = "MDC_DEMO_CANNOT_SLEEP_OPTION_CHOICE_ENUM_TYPE"
MDC_SLEEP_OPTION_CHOICE_ENUM_CANNOT_SLEEP_0 = "Not_during_the_Less_than_Once_or_twice_Three_or_more_past_month"
MDC_SLEEP_OPTION_CHOICE_ENUM_CANNOT_SLEEP_1 = "once_a_week"
MDC_SLEEP_OPTION_CHOICE_ENUM_CANNOT_SLEEP_2 = "a_week"
MDC_SLEEP_OPTION_CHOICE_ENUM_CANNOT_SLEEP_3 = "num_times_a_week"
MDC_SLEEP_OPTION_CHOICE_ENUM_CANNOT_SLEEP = [
    MDC_SLEEP_OPTION_CHOICE_ENUM_CANNOT_SLEEP_0,
    MDC_SLEEP_OPTION_CHOICE_ENUM_CANNOT_SLEEP_1,
    MDC_SLEEP_OPTION_CHOICE_ENUM_CANNOT_SLEEP_2,
    MDC_SLEEP_OPTION_CHOICE_ENUM_CANNOT_SLEEP_3,
]

UNSTABLE_SLEEP_OPTION = "MDC_UNSTABLE_SLEEP_OPTION_CHOICE"
CANNOT_SLEEP_OPTION_TYPE = "MDC_DEMO_UNSTABLE_SLEEP_OPTION_CHOICE_ENUM_TYPE"
MDC_SLEEP_OPTION_CHOICE_ENUM_UNSTABLE_SLEEP_0 = "Not_during_the_Less_than_Once_or_twice_Three_or_more_past_month"
MDC_SLEEP_OPTION_CHOICE_ENUM_UNSTABLE_SLEEP_1 = "once_a_week"
MDC_SLEEP_OPTION_CHOICE_ENUM_UNSTABLE_SLEEP_2 = "a_week"
MDC_SLEEP_OPTION_CHOICE_ENUM_UNSTABLE_SLEEP_3 = "num_times_a_week"
MDC_SLEEP_OPTION_CHOICE_ENUM_UNSTABLE_SLEEP = [
    MDC_SLEEP_OPTION_CHOICE_ENUM_UNSTABLE_SLEEP_0,
    MDC_SLEEP_OPTION_CHOICE_ENUM_UNSTABLE_SLEEP_1,
    MDC_SLEEP_OPTION_CHOICE_ENUM_UNSTABLE_SLEEP_2,
    MDC_SLEEP_OPTION_CHOICE_ENUM_UNSTABLE_SLEEP_3,
]

UNSTABLE_SLEEP_OPTION_TYPE = "MDC_UNSTABLE_SLEEP_OPTION_TYPE"

SLEEP_QUALITY_OPTION = "MDC_SLEEP_QUALITY_OPTION_CHOICE"
SLEEP_QUALITY_OPTION_TYPE = "MDC_DEMO_SLEEP_QUALITY_OPTION_CHOICE_ENUM_TYPE"
MDC_SLEEP_OPTION_CHOICE_ENUM_SLEEP_QUALITY_0 = "Very good"
MDC_SLEEP_OPTION_CHOICE_ENUM_SLEEP_QUALITY_1 = " Fairly good"
MDC_SLEEP_OPTION_CHOICE_ENUM_SLEEP_QUALITY_2 = "Fairly bad"
MDC_SLEEP_OPTION_CHOICE_ENUM_SLEEP_QUALITY_3 = "Very bad"
MDC_SLEEP_OPTION_CHOICE_ENUM_SLEEP_QUALITY = [
    MDC_SLEEP_OPTION_CHOICE_ENUM_SLEEP_QUALITY_0,
    MDC_SLEEP_OPTION_CHOICE_ENUM_SLEEP_QUALITY_1,
    MDC_SLEEP_OPTION_CHOICE_ENUM_SLEEP_QUALITY_2,
    MDC_SLEEP_OPTION_CHOICE_ENUM_SLEEP_QUALITY_3,
]



PROBLEMS_OPTION = "MDC_PROBLEMS_OPTION_CHOICE"
PROBLEMS_OPTION_TYPE = "MDC_DEMO_PROBLEMS_OPTION_CHOICE_ENUM_TYPE"
MDC_SLEEP_OPTION_CHOICE_ENUM_PROBLEMS_0 = "no_problem_at_all"
MDC_SLEEP_OPTION_CHOICE_ENUM_PROBLEMS_1 = "only_a_very_slight_problem"
MDC_SLEEP_OPTION_CHOICE_ENUM_PROBLEMS_2 = "somewhat_of_a_problem"
MDC_SLEEP_OPTION_CHOICE_ENUM_PROBLEMS_3 = "a_very_big_problem"
MDC_SLEEP_OPTION_CHOICE_ENUM_PROBLEMS = [
    MDC_SLEEP_OPTION_CHOICE_ENUM_PROBLEMS_0,
    MDC_SLEEP_OPTION_CHOICE_ENUM_PROBLEMS_1,
    MDC_SLEEP_OPTION_CHOICE_ENUM_PROBLEMS_2,
    MDC_SLEEP_OPTION_CHOICE_ENUM_PROBLEMS_3,
]

SNORE_LOUDLY = "MDC_VND_AIT_MODE_SNORE_LOUDLY"

SLEEPY_DAYTIME = "MDC_VND_AIT_MODE_SLEEPY_DAYTIME"

STOP_BREATH_INASLEEP = "MDC_VND_AIT_MODE_STOP_BREATH_INASLEEP"

IS_LARGE_SHIRT = "MDC_VND_AIT_MODE_IS_LARGE_SHIRT"

# --- health ----
HEALTH_ROOT = "MDC_DEV_SPEC_PROFILE_STU_BASELINE_HEALTH_ROOT"

HAD_DISEASES_OPTION = "MDC_HAD_DISEASES_OPTION_CHOICE"
HAD_DISEASES_OPTION_TYPE = "MDC_DEMO_HAD_DISEASES_OPTION_CHOICE_ENUM_TYPE"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_0 = "Skin_cancer"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_1 = "Other_cancers"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_2 = "Heart_disease_"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_3 = "High_blood_pressure"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_4 = "High_cholesterol"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_5 = "Stroke"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_6 = "Diabetes __type_1"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_7 = "Diabetes___type_2_or_unsure"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_8 = "Enlarged_prostate_M"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_9 = "Asthma"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_10 = "Hay_fever"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_11 = "Arthritis"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_12 = "Depression"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_13 = "Anxiety"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_14 = "Chronic_obstructive_pulmonary_disease_COPD"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_15 = "Obstructive_sleep_apnoea"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_16 = "Back_pain"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_17 = "None_of_these"
MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES = [
    MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_0,
    MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_1,
    MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_2,
    MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_3,
    MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_4,
    MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_5,
    MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_6,
    MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_7,
    MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_8,
    MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_9,
    MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_10,
    MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_11,
    MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_12,
    MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_13,
    MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_14,
    MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_15,
    MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_16,
    MDC_SLEEP_OPTION_CHOICE_ENUM_HAD_DISEASES_17,
]

HAS_OTHER_ILLNESS = "MDC_VND_AIT_MODE_HAS_OTHER_ILLNESS"

ILLNESS = "MDC_VND_AIT_MODE_ILLNESS"

#----wellbeing----
WELLBEING_ROOT = "MDC_DEV_SPEC_PROFILE_STU_BASELINE_WELLBEING_ROOT"

FEELING_FREQUENCY_OPTION = "MDC_FEELING_FREQUENCY_OPTION_CHOICE"
FEELING_FREQUENCY_OPTION_TYPE = "MDC_DEMO_FEELING_FREQUENCY_OPTION_CHOICE_ENUM_TYPE"
MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCY_0 = "All_of_the_time"
MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCY_1 = "most_of_the_time"
MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCY_2 = "some_of_the_time"
MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCY_3 = "a_little_of_the_time"
MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCY_4 = "none_of_the_time"
MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCY = [
    MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCY_0,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCY_1,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCY_2,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCY_3,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCY_4,
]

NERVOUS_OPTION = "MDC_NERVOUS_OPTION_CHOICE"

HOPELESS_OPTION = "MDC_HOPELESS_OPTION_CHOICE"

FIDGETY_OPTION = "MDC_FIDGETY_OPTION_CHOICE"

DEPRESSED_OPTION = "MDC_DEPRESSED_OPTION_CHOICE"

EXHUASTED_OPTION = "MDC_EXHUASTED_OPTION_CHOICE"

WORTHLESS_OPTION = "MDC_WORTHLESS_OPTION_CHOICE"

NAE_OPTION = "MDC_NAE_OPTION_CHOICE"

#BOTHERED_FREQUENCY_OPTION = "MDC_BOTHERED_FREQUENCY_OPTION_CHOICE"
BOTHERED_FREQUENCY_OPTION_TYPE = "MDC_WELLBEING_BOTHERED_FREQUENCY_OPTION_CHOICE_ENUM_TYPE"
MDC_WELLBEING_OPTION_CHOICE_ENUM_BOTHERED_FREQUENCY_0 = "Not_at_all_sure"
MDC_WELLBEING_OPTION_CHOICE_ENUM_BOTHERED_FREQUENCY_1 = "several_days"
MDC_WELLBEING_OPTION_CHOICE_ENUM_BOTHERED_FREQUENCY_2 = "over_half_the_days"
MDC_WELLBEING_OPTION_CHOICE_ENUM_BOTHERED_FREQUENCY_3 = "nearly_every_day"
MDC_WELLBEING_OPTION_CHOICE_ENUM_BOTHERED_FREQUENCY = [
    MDC_WELLBEING_OPTION_CHOICE_ENUM_BOTHERED_FREQUENCY_0,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_BOTHERED_FREQUENCY_1,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_BOTHERED_FREQUENCY_2,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_BOTHERED_FREQUENCY_3,
]

KEEP_WORRYING_OPTION = "MDC_NAE_KEEP_WORRYING_OPTION"

WORRYING_ALOT_OPTION = "MDC_NAE_WORRYING_ALOT_OPTION"

TROUBLE_RELAXING_OPTION = "MDC_NAE_TROUBLE_RELAXING_OPTION"

RESTLESS_OPTION = "MDC_NAE_RESTLESS_OPTION"

EASILY_ANNOYED_OPTION = "MDC_NAE_EASILY_ANNOYED_OPTION"

PASSIVE_THINKING_OPTION = "MDC_NAE_PASSIVE_THINKING_OPTION"

LIL_PLEASURE_OPTION = "MDC_NAE_LIL_PLEASURE_OPTION"

DDH_OPTION = "MDC_NAE_DDH_OPTION"

SLEEP_PROBLEM_OPTION = "MDC_NAE_SLEEP_PROBLEM_OPTION"

LIL_ENERGY_OPTION = "MDC_NAE_LIL_ENERGY_OPTION"

EAT_PROBLEM_OPTION = "MDC_NAE_EAT_PROBLEM_OPTION"

POOR_SELF_JUDGEMENT_OPTION = "MDC_NAE_POOR_SELF_JUDGEMENT_OPTION"

CANNOT_CONCENTRATE_OPTION = "MDC_NAE_CANNOT_CONCENTRATE_OPTION"

AWKWARD_ACTION_OPTION = "MDC_NAE_AWKWARD_ACTION_OPTION"

SUICIDE_THOUGHT_OPTION = "MDC_NAE_SUICIDE_THOUGHT_OPTION"

BOTHERING_PROBLEMS_1_DIFFICULTY_OPTION = "MDC_NAE_BOTHERING_PROBLEMS_1_DIFFICULTY_OPTION"

BOTHERING_PROBLEMS_2_DIFFICULTY_OPTION = "MDC_NAE_BOTHERING_PROBLEMS_2_DIFFICULTY_OPTION"


DIFFICULTY_OPTION_TYPE = "MDC_WELLBEING_DIFFICULTY_OPTION_CHOICE_ENUM_TYPE"
MDC_WELLBEING_OPTION_CHOICE_ENUM_DIFFICULTY_0 = "Not_difficult_at_all"
MDC_WELLBEING_OPTION_CHOICE_ENUM_DIFFICULTY_1 = "Somewhat_difficult"
MDC_WELLBEING_OPTION_CHOICE_ENUM_DIFFICULTY_2 = "Very_Difficult"
MDC_WELLBEING_OPTION_CHOICE_ENUM_DIFFICULTY_3 = "Extremely_Difficult"
MDC_WELLBEING_OPTION_CHOICE_ENUM_DIFFICULTY = [
    MDC_WELLBEING_OPTION_CHOICE_ENUM_DIFFICULTY_0,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_DIFFICULTY_1,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_DIFFICULTY_2,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_DIFFICULTY_3,
]

HANGOUT_TIME = "MDC_STU_HANGOUT_TIME"

CALLING_TIME = "MDC_STU_CALLING_TIME"

MEETINGS_TIME = "MDC_STU_MEETINGS_TIME"

NEAR_FRIENDS = "MDC_STU_NEAR_FRIENDS"

#[Never, rarely, sometimes, often, always, N/A]
OCCURING_FREQUENCY_OPTION_TYPE = "MDC_WELLBEING_OCCURING_FREQUENCY_OPTION_CHOICE_ENUM_TYPE"
MDC_WELLBEING_OPTION_CHOICE_ENUM_OCCURING_FREQUENCY_0 = "Never"
MDC_WELLBEING_OPTION_CHOICE_ENUM_OCCURING_FREQUENCY_1 = "rarely"
MDC_WELLBEING_OPTION_CHOICE_ENUM_OCCURING_FREQUENCY_2 = "sometimes"
MDC_WELLBEING_OPTION_CHOICE_ENUM_OCCURING_FREQUENCY_3 = "often"
MDC_WELLBEING_OPTION_CHOICE_ENUM_OCCURING_FREQUENCY_4 = "always"
MDC_WELLBEING_OPTION_CHOICE_ENUM_OCCURING_FREQUENCY_5 = "N_A"
MDC_WELLBEING_OPTION_CHOICE_ENUM_OCCURING_FREQUENCY = [
    MDC_WELLBEING_OPTION_CHOICE_ENUM_OCCURING_FREQUENCY_0,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_OCCURING_FREQUENCY_1,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_OCCURING_FREQUENCY_2,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_OCCURING_FREQUENCY_3,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_OCCURING_FREQUENCY_4,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_OCCURING_FREQUENCY_5,
]

CARED_PARTNER_OPTION = "MDC_STU_CARED_PARTNER_OPTION"

DEMANDING_PARTNER_OPTION = "MDC_STU_DEMANDING_PARTNER_OPTION"

CARED_FAMILY_OPTION = "MDC_STU_CARED_FAMILY_OPTION"

DEMANDING_FAMILY_OPTION = "MDC_STU_DEMANDING_FAMILY_OPTION"

DEMANDING_FRIENDS_OPTION = "MDC_STU_DEMANDING_FRIENDS_OPTION"

CARED_CO_WORKERS_OPTION = "MDC_STU_CARED_CO_WORKERS_OPTION"

DEMANDING_CO_WORKERS_OPTION = "MDC_STU_DEMANDING_CO_WORKERS_OPTION"

INTEREST_FROM_CO_WORKERS_OPTION = "MDC_STU_INTEREST_FROM_CO_WORKERS_OPTION"

CRITICISING_CO_WORKERS_OPTION = "MDC_STU_CRITICISING_CO_WORKERS_OPTION"

CONFLICT_WITH_CO_WORKERS_OPTION = "MDC_STU_CONFLICT_WITH_CO_WORKERS_OPTION"


HAD_HEALTHCARE_PLACE = "MDC_VND_AIT_MODE_HAD_HEALTHCARE_PLACE"


HEALTHCARE_PLACE_OPTION = "MDC_HEALTHCARE_PLACE_OPTION_CHOICE"
HEALTHCARE_PLACE_OPTION_TYPE = "MDC_WELLBEING_HEALTHCARE_PLACE_OPTION_CHOICE_ENUM_TYPE"
MDC_WELLBEING_OPTION_CHOICE_ENUM_HEALTHCARE_PLACE_0 = "GP_or_family_doctor_clinic"
MDC_WELLBEING_OPTION_CHOICE_ENUM_HEALTHCARE_PLACE_1 = "Hospital_emergency_department"
MDC_WELLBEING_OPTION_CHOICE_ENUM_HEALTHCARE_PLACE_2 = "Hospital_outpatient_clinic"
MDC_WELLBEING_OPTION_CHOICE_ENUM_HEALTHCARE_PLACE_3 = "Medical_specialist_clinic"
MDC_WELLBEING_OPTION_CHOICE_ENUM_HEALTHCARE_PLACE_4 = "Other"
MDC_WELLBEING_OPTION_CHOICE_ENUM_HEALTHCARE_PLACE = [
    MDC_WELLBEING_OPTION_CHOICE_ENUM_HEALTHCARE_PLACE_0,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_HEALTHCARE_PLACE_1,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_HEALTHCARE_PLACE_2,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_HEALTHCARE_PLACE_3,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_HEALTHCARE_PLACE_4,
]

IMMEDIATE_APPOINTMENT = "MDC_STU_IMMEDIATE_APPOINTMENT"
KNOW_MEDI_HISTORY = "MDC_STU_KNOW_MEDI_HISTORY"
COORDINATION = "MDC_STU_COORDINATION"


# -------------------- daily survey -----------------
DAILY_WELLBEING_ROOT = "MDC_DEV_SPEC_PROFILE_STU_DAILY_WELLBEING_ROOT"

FEELING_FREQUENCIES_OPTION_TYPE = "MDC_DAILY_WELLBEING_FEELING_FREQUENCIES_OPTION_CHOICE_ENUM_TYPE"
MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCIES_0 = "Not_at_all"
MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCIES_1 = "Less_than_half_the_time"
MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCIES_2 = "More_than_half_the_time"
MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCIES_3 = "All_of_the_time"
MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCIES = [
    MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCIES_0,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCIES_1,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCIES_2,
    MDC_WELLBEING_OPTION_CHOICE_ENUM_FEELING_FREQUENCIES_3,
]

DAILY_NAE_OPTION = "MDC_DAILY_NAE_OPTION_CHOICE"

DAILY_KEEP_WORRYING_OPTION = "MDC_DAILY_KEEP_WORRYING_OPTION_CHOICE"

DAILY_DDH_OPTION = "MDC_DAILY_DAILY_DDH_OPTION_CHOICE"

DAILY_LIL_PLEASURE_OPTION = "MDC_DAILY_DAILY_LIL_PLEASURE_OPTION_CHOICE"

FEELING_RN = "MDC_STU_FEELING_RN"

SATISFACTION = "MDC_STU_SATISFACTION"

PHYSICAL_PAIN = "MDC_STU_PHYSICAL_PAIN"

PHYSICAL_PAIN_LVL = "MDC_STU_PHYSICAL_PAIN_LVL"


# -- diet ---
DAILY_DIET_ROOT = "MDC_DEV_SPEC_PROFILE_STU_DAILY_DIET_ROOT"

DAILY_SERVES_OF_FRUIT = "MDC_STU_DAILY_SERVES_OF_FRUIT"

DAILY_SERVES_OF_VEGE = "MDC_STU_DAILY_SERVES_OF_VEGE"

DAILY_CUPS_OF_SOFT_DRINKS = "MDC_STU_DAILY_CUPS_OF_SOFT_DRINKS"

DAILY_CUPS_OF_CAFFEINE_DRINKS = "MDC_STU_DAILY_CUPS_OF_CAFFEINE_DRINKS"

DAILY_MEALS_OF_BURGERS = "MDC_STU_DAILY_MEALS_OF_BURGERS"

DAILY_SERVES_OF_FRIES = "MDC_STU_DAILY_SERVES_OF_FRIES"

DAILY_SERVES_OF_SALTY_SNACKS = "MDC_STU_DAILY_SERVES_OF_SALTY_SNACKS"

DAILY_SERVES_OF_SWEET_SNACKS = "MDC_STU_DAILY_SERVES_OF_SWEET_SNACKS"

DAILY_SERVES_OF_CONFECTIONARY = "MDC_STU_DAILY_SERVES_OF_CONFECTIONARY"


# --- alcohol and smoking
DAILY_ALCOHOL_SMOKING_ROOT = "MDC_DEV_SPEC_PROFILE_STU_DAILY_ALCOHOL_SMOKING_ROOT"

DAILY_STANDARD_ALCOHOLIC_DRINKS = "MDC_STU_DAILY_STANDARD_ALCOHOLIC_DRINKS"

DAILY_CIGARETTES = "MDC_STU_DAILY_CIGARETTES"

# --- physical activity --- 
DAILY_PHYSICAL_ACTIVITY_ROOT = "MDC_DEV_SPEC_PROFILE_STU_DAILY_PHYSICAL_ACTIVITY_ROOT"

#units
MDC_DAILY_MINS = "MDC_DAILY_MINS"

MDC_DAILY_HOURS = "MDC_DAILY_HOURS"

DAILY_VIGOROUS_ACTIVITY = "MDC_STU_DAILY_VIGOROUS_ACTIVITY"

DAILY_MODERATE_ACTIVITY = "MDC_STU_DAILY_MODERATE_ACTIVITY"

DAILY_SEDENTARY_ACTIVITY = "MDC_STU_DAILY_SEDENTARY_ACTIVITY"

# -- sleep ----
DAILY_SLEEP_ROOT = "MDC_DEV_SPEC_PROFILE_STU_DAILY_SLEEP_ROOT"

MDC_DAILY_TIME = "MDC_DAILY_TIME"

DAILY_BED_TIME = "MDC_STU_DAILY_BED_TIME"

DAILY_ASLEEP_TIME = "MDC_STU_DAILY_ASLEEP_TIME"

DAILY_WAKEUP_TIME = "MDC_STU_DAILY_WAKEUP_TIME"

ALARM_USED = "MDC_STU_ALARM_USED"

DAILY_SLEEP_QUALITY = "MDC_STU_DAILY_SLEEP_QUALITY"


# --- work ---
DAILY_WORK_ROOT = "MDC_DEV_SPEC_DAILY_WORK_ROOT"

IS_WORK_DAY = "MDC_STU_IS_WORK_DAY"

DAILY_WORK_HOURS = "MDC_STU_DAILY_WORK_HOURS"

SHIFT_TIME_OPTION = "MDC_SHIFT_TIME_OPTION_CHOICE"
SHIFT_TIME_OPTION_TYPE = "MDC_DAILY_WORK_SHIFT_TIME_OPTION_CHOICE_ENUM_TYPE"
MDC_DAILY_WORK_OPTION_CHOICE_ENUM_SHIFT_TIME_0 = "during_the_day"
MDC_DAILY_WORK_OPTION_CHOICE_ENUM_SHIFT_TIME_1= "during_the_night"
MDC_DAILY_WORK_OPTION_CHOICE_ENUM_SHIFT_TIME = [
    MDC_DAILY_WORK_OPTION_CHOICE_ENUM_SHIFT_TIME_0,
    MDC_DAILY_WORK_OPTION_CHOICE_ENUM_SHIFT_TIME_1,
]

HEALTSCORE_ROOT = "MDC_DEV_SPEC_PROFILE_STU_HEALTHSCORE"

WELLBEING_SCORE = "MDC_STU_WELLBEING_SCORE"

DIET_SCORE = "MDC_STU_DIET_SCORE"

ALCOHOL_SMOKING_SCORE = "MDC_STU_ALCOHOL_SMOKING_SCORE"

PA_SCORE = "MDC_STU_PA_SCORE"

SLEEP_SCORE = "MDC_STU_SLEEP_SCORE"

FINAL_HEALTHSCORE = "MDC_STU_FINAL_HEALTHSCORE"

# ------------ CHART --------------

CHART_CATEGORY__PHYSICALACTIVITY = "PHYSICALACTIVITY"

CHART_CATEGORY__SLEEP = "SLEEP"

CHART_CATEGORY__HEALTHSCORE = "HEALTHSCORE"

CHART_NAME__SIMPLE_HS_CHART = "SIMPLEHEALTHSCORE"

