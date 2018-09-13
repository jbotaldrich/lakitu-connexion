from swagger_server.models.parameter_description import ParameterDescription
from swagger_server.models.run_status import RunStatus
from swagger_server.models.run_results import RunResults
from swagger_server.models.run_submission import RunSubmission
from swagger_server.models.pipelines import Pipelines
from swagger_server.models.conda_source import CondaSource
from swagger_server.models.pipeline import Pipeline

import lakitu.server as lakitu_impl


def service_specific_init(app):
    lakitu_impl.extra_init(app)
    lakitu_impl.start_luigi()
    return

class DevelopersController_impl(object):

    @staticmethod
    def get_run_status(runId):
        return RunStatus(run_status=lakitu_impl.check_run(runId))

    @staticmethod
    def get_run_results(runId):  # noqa: E501
        return abort(501) # Not implemented.

    @staticmethod
    def list_pipeline_parameters(name, version):  # noqa: E501
        entry_array = lakitu_impl.pipeline_parameters(name, version)
        parameter_descriptions = [ ParameterDescription(help_description=entry[lakitu_impl.LUIGI_HELP], 
            parameter_name=entry[lakitu_impl.LUIGI_PARAMETER]) for entry in entry_array]

        return parameter_descriptions

    @staticmethod
    def list_pipelines():  # noqa: E501
        return Pipelines.from_dict(lakitu_impl.list_pipelines())

    @staticmethod
    def run_pipeline(name, version, parameters):  # noqa: E501
        lakitu_format_parameters = []
        # Lakitu needs the parameters in a list form.
        for parameter in parameters:
            lakitu_format_parameters.append(parameter.parameter_name)
            lakitu_format_parameters.append(parameter.parameter_value)
        run_id = lakitu_impl.run_pipeline(name, version, lakitu_format_parameters)
        return RunSubmission(run_id=run_id)