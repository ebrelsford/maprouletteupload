import click
import json

from .api import get_challenge, upload_tasks
from .tasks import create_tasks

# TODO use api to optionally create challenge too
# TODO use api to figure out which tasks already exist

@click.command()
@click.option('--api-key', help='Your API key, via Maproulette.')
@click.option('--challenge-id', type=int,
        help='The challenge ID these tasks should be added to.')
@click.option('--identifier', type=str, default='identifier',
        help=('The name of the property to use as the identifier. Default: '
            '"identifier".'))
@click.option('--instruction', type=str, default='instruction',
        help=('The name of the property to use as the instruction. Default: '
            '"instruction".'))
@click.option('--name', type=str, default='name',
        help=('The name of the property to use as the name. Default: "name".'))
@click.option('--geojson-file', type=click.Path(exists=True),
        help=('A GeoJSON file of tasks to upload. Alternatively, you can '
            'provide this file via stdin.'))
@click.version_option()
def upload(api_key, challenge_id, identifier, instruction, name, geojson_file):
    """Upload a GeoJSON file (or stdin) of tasks to Maproulette."""
    if not api_key:
        raise click.BadParameter('API key required. Please try again.')
    if not challenge_id:
        raise click.BadParameter('Challenge ID required. Please try again.')
    if geojson_file:
        geojson = json.load(open(geojson_file, 'r'))
    else:
        geojson = json.load(click.get_text_stream('stdin'))

    challenge = get_challenge(challenge_id)
    if challenge is None:
        click.echo('Challenge does not exist. Quitting.')
        return

    create_tasks_kwargs = {
        'identifier_field': identifier,
        'instruction_field': instruction,
        'name_field': name,
    }

    tasks = list(create_tasks(geojson, **create_tasks_kwargs))
    response = upload_tasks(api_key, challenge_id, tasks)
    click.echo('Done uploading tasks. Status code: %d' % response.status_code)
    click.echo(response.text)


if __name__ == '__main__':
    upload()
