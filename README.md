# maprouletteupload

Simply upload a GeoJSON file of tasks to [Maproulette](http://maproulette.org/).

## Features

Uses the [Maproulette API](https://github.com/maproulette/maproulette2/blob/master/docs/api.md) to:
* Create a challenge if you don't already have one.
* Create a task for each GeoJSON feature, pulling per-task identifiers and instructions out of the feature's properties.

## Installation

```
pip install maprouletteupload
```

## Usage

Use via the command line:

```
Usage: maprouletteupload [OPTIONS]

  Upload a GeoJSON file of tasks to Maproulette.

Options:
  --api-key TEXT          Your API key, via Maproulette.
  --challenge-id INTEGER  The challenge ID these tasks should be added to. If
                          not specified you will be prompted to create one.
  --geojson-file TEXT     A GeoJSON file of tasks to upload. Alternatively,
                          you can provide this file via stdin.
  --identifier TEXT       The name of the property to use as the identifier.
                          Default: "identifier".
  --instruction TEXT      The name of the property to use as the instruction.
                          Default: "instruction".
  --name TEXT             The name of the property to use as the name.
                          Default: "name".
  --version               Show the version and exit.
  --help                  Show this message and exit.

```

A task is made for each GeoJSON feature and the tasks are bulk uploaded to Maproulette.

## Example

If you have GeoJSON of tasks and have not created a challenge in Maproulette, you could create a challenge (you will be prompted for details) and upload the tasks by using:


```
maprouletteupload --api-key [YOUR_API_KEY] < tasks.geojson
```

## License

MIT.
