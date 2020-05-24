# LDTC
LDTC, Language-Detecting Text Classifier, is a pure Python trainable language
detector with no external dependencies.

## CLI Tool
If you just want to do some simple detection on the command line, use the
CLI tool. To use an existing model, <!-- When initialising a Classifier
object, pass in the keyword argument `supress_uncompiled_model_warning=True`.
-->use `ldtc <modelfile>`. It will prompt for a string, and classify it,
outputting the language on stdout (or "unknown" if it cannot determine
anything) See "Model format" for a description of the model. To compile a
model, use `ldtc <rawmodelfile> -c|--compile <compiledmodelfile>`.

## Library
If you want to use LDTC programmatically, use the library.
### `ldtc.Classifier(model)`
Create a `Classifier` object using the given model (as a Python list/dict, not
as JSON). If the model is raw (a list), it will print a big warning on stderr.
### `Classifier.check(text)`
Detect language of `text` with using the model used to instantiate the
`Classifier`. Returns the language LDTC believes the text is in (as a string),
or `'unknown'` when it cannot classify the text.

## Model format
Since you never really need to mess with compiled models, I won't discuss
them. You can read the code if you really need to figure them out.

This section explains the raw model format, which is how you should create and
edit models.

Raw models are formatted as a list of dicts. See below for the format:

    [
        {
            "text": "<text in the language>",
            "category": "<the language>"
        }
    ]

Note that the attribute for the language name is `category`, **not**
`language`.

Although LDTC handles models as Python lists (for raw models) or dicts (for
compiled models), I recommend storing them in JSON format, mainly because the
command-line tool uses JSON.

You can use a raw model anywhere you can use a compiled model. However, both
the library and the CLI tool will print a big warning to stderr if you do
this. There is a comment in a random place in this document explaining how to
disable this in the library. (It's in a comment so you can't do it without
some effort.) The warning cannot be disabled in the CLI program without
hacking the source.

<!-- ## Example models
I provide an example model trained to distinguish between texts written by
Mark Twain and those written by William Shakespeare. I chose them because
their works have all gone into the public domain, and their writing style is
so different that LDTC can easily tell the difference, making it a good
demonstration.

The raw model is in `twain_shakespeare_raw.json`; the compiled model is in
`twain_shakespeare.json`. -->
