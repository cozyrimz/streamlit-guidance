from src.config import GUIDANCE_SERVER_URL
from typing import Any
import requests

def get_companies() -> Any:
    """
    Returns a list of companies that the server contains valid guidance for
    """
    url = f"{GUIDANCE_SERVER_URL}/api/v1/guidance/companies"
    response = requests.get(url)
    return response.json()['companies']

def get_company_guidance_periods(ticker) -> Any:
    """
    Returns a list periods that the server contains valid guidance for given a company ticker
    """
    url = f"{GUIDANCE_SERVER_URL}/api/v1/guidance/periods/{ticker}"
    response = requests.get(url)
    return response.json()['periods']

def get_company_guidance(company, year, quarter) -> Any:
    """
    Returns a guidance for a company in a particular period
    """
    url = f"{GUIDANCE_SERVER_URL}/api/v1/guidance"

    query_params = {'companyTicker':company, 'year':year, 'quarter':quarter}
    req = requests.models.PreparedRequest()
    req.prepare_url(url, query_params)
    # print(req.url)

    response = requests.get(req.url)


    return response.json()['guidance']