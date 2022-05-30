import phoebe
# if phoebe.__version__ != '2.4.0':
#     raise ImportError("PHOEBE version is not 2.4.0")
import numpy as np
b = phoebe.default_binary()
b.set_value('incl@binary', 85)
b.add_dataset('lc', compute_times=phoebe.linspace(0,1,101))
b.run_compute()
#b.add_compute('ellc')
#b.set_value_all('ld_mode', 'lookup')
#b.run_compute(kind='ellc')
b.set_value('times@dataset', b.get_value('times@model'))
b.set_value('fluxes@dataset', b.get_value('fluxes@model'))
b.set_value('sigmas@dataset', np.ones_like(b.get_value('fluxes@model'))*0.01)
b.add_solver('estimator.ebai', ebai_method='mlp', solver='mlp_solver')
b.run_solver('mlp_solver')
b.add_solver('estimator.ebai', ebai_method='knn', solver='knn_solver')
b.run_solver('knn_solver')

b.set_value('times@dataset', b.get_value('times@model').flatten()[::20])
b.set_value('fluxes@dataset', b.get_value('fluxes@model').flatten()[::20])
b.set_value('sigmas@dataset', np.ones_like(b.get_value('fluxes@model').flatten()[::20])*0.01)

b.add_distribution('incl@binary', phoebe.uniform(85,90), distribution='mydist')
b.run_compute(sample_from='mydist', sample_num=3)

b.add_solver('optimizer.nelder_mead', fit_parameters='incl@binary', maxiter=10, maxfev=20, solver='nm_solver')
b.run_solver('nm_solver')
b.add_solver('sampler.emcee', init_from='mydist', nwalkers=4, niters=5, solver='emcee_solver')
b.run_solver('emcee_solver')

b.add_gaussian_process('sklearn')
b.run_compute(model='with_sklearn_gp')
b.disable_feature('gp_sklearn01')
b.add_gaussian_process('celerite2')
b.run_compute(model='with_celerite2_gp')
#b.run_solver('emcee_solver', detach=True)
#b.attach_job()
