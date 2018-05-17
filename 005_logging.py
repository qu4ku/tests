import logging


def sample_function(param):
	logger = logging.getLogger(__name__)
	logger.debug('Going to perform magic with {}'.format(param))

	try:
		result = do_magic(param)
	except IndexError:
		logger.exceptin('OMG it happened again, somone please tell Kamil')
	except:
		logger.info('Unexpected exception', exc_info=True)
		raise
	else:
		logger.info('Magic with {} resulted in {}'.format(param, result, stack_info=True))

sample_function('som')