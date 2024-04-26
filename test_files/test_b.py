# Make sure endpoint are immune to missing trailing slashes
api_router = APIRouter(redirect_slashes=True)