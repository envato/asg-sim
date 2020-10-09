from asgsim.model import Model, run_model
from asgsim.plots.utils import make_scaling_plot
params = {'builder_boot_time': 70,
           'builds_per_hour': 924,
           'build_run_time': 334,
           'builds_per_hour_fn': Model.SINE,
           'autoscale': True,
           'alarm_period_duration': 10,
           'scale_up_alarm_period_count': 1,
           'scale_down_alarm_period_count': 5,
           'scale_up_threshold': 1,
           'scale_down_threshold': 6,
           'scale_up_change': 8,
           'scale_down_change': 1,
           'initial_builder_count': 16,
           'max_size': 120,
           'min_size': 16,
           'sec_per_tick': 10,
           'ticks': 9000}

m = run_model(**params)
print(m.mean_queue_time())
print(m.percentile_queue_time(95.0))
print(m.max_build_queue_length())
make_scaling_plot(params, 'My Scaling Plot', 'fig')
