SUFIJOS = { 1000: ['KB','MB','GB','TB','PB','EB','ZB','YB'], 1024: ['KiB','MiB', 'GiB','TiB','PiB','EiB','ZiB','YiB']}

def tamanyo_aproximado(tamanyo, un_kilobyte_es_1024_bytes=True):
	'''C o n v i e r t e un tamaño de f i c h e r o en formato l e g i b l e por p e r s o n a s'''

	if tamanyo < 0:
		raise ValueError('El número no puede ser negativo')

	multiplo = 1024 if un_kilobyte_es_1024_bytes else 1000
	for sufijo in SUFIJOS[multiplo]:
		tamanyo /= multiplo
		if tamanyo < multiplo:
			return '{0:.1f} {1}'.format(tamanyo, sufijo)

	raise ValueError( 'Número demasiado grande')

if __name__ == '__main__':
	print(tamanyo_aproximado(1000000000000,False))
	print(tamanyo_aproximado(1000000000000))
