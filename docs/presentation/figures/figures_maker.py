# %%
from pathlib import Path
from goa import problems, algorithms

figures_dir = Path('.')

# %%
p = problems.Ackley(bounds=(-2., 2.))
fig, ax = p.plot(cmap='Reds_r', view_init=(30, 120))
fig.savefig(figures_dir / '01-ackley.png')
p = problems.Ackley(bounds=(-2., 2.))
fig, ax = p.plot(cmap='Reds_r', view_init=(0, 120))
fig.savefig(figures_dir / '02-ackley.png')

# %%
p = problems.Rastrigin(bounds=(-5., 5.))
fig, ax = p.plot(cmap='Blues_r', view_init=(45, 120))
fig.savefig(figures_dir / '01-rastrigin.png')
p = problems.Rastrigin(bounds=(-5., 5.))
fig, ax = p.plot(cmap='Blues_r', view_init=(0, 120))
fig.savefig(figures_dir / '02-rastrigin.png')

# %%

