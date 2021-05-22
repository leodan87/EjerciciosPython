import wikipedia
wikipedia.set_lang('es')
print(wikipedia.summary('javascript',sentences=2))
