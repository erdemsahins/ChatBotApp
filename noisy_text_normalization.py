from os.path import join

from jpype import JClass, JString, getDefaultJVMPath, shutdownJVM, startJVM


def Normalize(query):
    ZEMBEREK_PATH: str = join('Zemberek','bin', 'zemberek-full.jar')

    startJVM(
        getDefaultJVMPath(),
        '-ea',
        f'-Djava.class.path={ZEMBEREK_PATH}',
        convertStrings=False
    )

    TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
    TurkishSentenceNormalizer: JClass = JClass(
        'zemberek.normalization.TurkishSentenceNormalizer'
    )
    Paths: JClass = JClass('java.nio.file.Paths')

    normalizer = TurkishSentenceNormalizer(
        TurkishMorphology.createWithDefaults(),
        Paths.get(
            join('Zemberek','ZemberekData', 'normalization')
        ),
        Paths.get(
            join('Zemberek','ZemberekData', 'lm', 'lm.2gram.slm')
        )
    )


    norm = normalizer.normalize(JString(query))

    print((
        f'\nNoisy : {query}'
        f'\nNormalized : {normalizer.normalize(JString(query))}\n'
    ))


    return norm

    shutdownJVM()

