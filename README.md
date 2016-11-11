# maprouletteupload

Simply upload a GeoJSON file of tasks to [Maproulette](http://maproulette.org/).

## Installation

## Usage

Use via the command line:

```
Usage: maprouletteupload [OPTIONS]

Options:
  --api-key TEXT          Your API key, via Maproulette.
  --challenge-id INTEGER  The challenge ID these tasks should be added to.
  --geojson-file TEXT     A GeoJSON file of tasks to upload. Alternatively,
                          you can provide this file via stdin.
  --identifier TEXT       The name of the property to use as the identifier
  --instruction TEXT      The name of the property to use as the instruction
  --name TEXT             The name of the property to use as the name
  --version               Show the version and exit.
  --help                  Show this message and exit.

```

A task is made for each GeoJSON feature and the tasks are bulk uploaded to Maproulette.


## License

MIT.
