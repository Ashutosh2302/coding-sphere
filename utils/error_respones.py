from pydantic import BaseModel

class ErrorResponse(BaseModel):
    detail: str

all_error_responses = {
    400: {"description": "Bad request", "model": ErrorResponse},
    401: {"description": "Unauthorized", "model": ErrorResponse},
    403: {"description": "Forbidden", "model": ErrorResponse},
    500: {"description": "An unexpected error occurred", "model": ErrorResponse}
}


login_error_responses = {500: all_error_responses[500]}

register_error_responses = {
    400: all_error_responses[400],
    500: all_error_responses[500]
}

get_project_error_respones = {
    400: all_error_responses[400],
    401: all_error_responses[401],
    500: all_error_responses[500]
}

get_projects_error_respones = {
    401: all_error_responses[401],
    500: all_error_responses[500]
}

create_project_error_respones = {
    400: all_error_responses[400],
    401: all_error_responses[401],
    403: all_error_responses[403],
    500: all_error_responses[500]
}

update_project_error_respones = create_project_error_respones.copy()
delete_project_error_respones = create_project_error_respones.copy()