import click
import json

from .tasks import create_tasks
from .upload import upload_tasks

# TODO use api to optionally create challenge too
# TODO use api to figure out which tasks already exist

@click.command()
@click.option('--api-key', help='Your API key, via Maproulette.')
@click.option('--challenge-id', type=int,
        help='The challenge ID these tasks should be added to.')
@click.option('--geojson-file',
        help=('A GeoJSON file of tasks to upload. Alternatively, you can '
            'provide this file via stdin.'))
@click.option('--identifier', type=str, default='identifier',
        help=('The name of the property to use as the identifier. Default: '
              '"identifier".'))
@click.option('--instruction', type=str, default='instruction',
        help=('The name of the property to use as the instruction. Default: '
              '"instruction".'))
@click.option('--name', type=str, default='name',
        help=('The name of the property to use as the name. Default: "name".'))
@click.version_option()
def upload(api_key, challenge_id, geojson_file, identifier, instruction, name):
    """Upload a GeoJSON file of tasks to Maproulette."""
    if not api_key:
        raise click.BadParameter('API key required. Please try again.')
    if not challenge_id:
        raise click.BadParameter('Challenge ID required. Please try again.')
    if geojson_file:
        geojson = json.load(open(geojson_file, 'r'))
    else:
        geojson = json.load(click.get_text_stream('stdin'))

    create_tasks_kwargs = {
        'identifier_field': identifier,
        'instruction_field': instruction,
        'name_field': name,
    }

    tasks = list(create_tasks(geojson), **create_tasks_kwargs)
    response = upload_tasks(api_key, challenge_id, tasks)
    click.echo('Done uploading tasks. Status code: %d' % response.status_code)
    click.echo(response.text)


if __name__ == '__main__':
    upload()
