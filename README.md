# Django-API


## Development

Clone the repository in local directory using-

```bash
git clone https://github.com/Darksoul98/Django-API.git
```

Install the requirements using-
```bash
pip install -r requirements.txt
```
### API
Base URL- [http://bhuvneshgupta.pythonanywhere.com](http://bhuvneshgupta.pythonanywhere.com)

Endpoint - /user

Method - GET

Response 
```bash
{
    "ok": true,
    "message": [
        {
            "id": "57dd4fe8-56bd-4adc-ada8-d74779593446",
            "real_name": "Egon Spengler",
            "tz": "America/Los_Angeles",
            "activity_periods": [
                {
                    "start_time": "2020-07-06T21:30:07.167176Z",
                    "end_time": "2020-07-06T21:30:07.167255Z"
                },
                {
                    "start_time": "2020-07-06T21:48:25.197025Z",
                    "end_time": "2020-07-06T21:48:25.197036Z"
                },
                {
                    "start_time": "2020-07-06T21:48:36.149164Z",
                    "end_time": "2020-07-06T21:48:36.149216Z"
                }
            ]
        },
        {
            "id": "399c7c45-fcf6-43d3-94df-d5f47d297d54",
            "real_name": "Glinda Southgood",
            "tz": "Asia/Kolkata",
            "activity_periods": [
                {
                    "start_time": "2020-07-06T21:49:52.926234Z",
                    "end_time": "2020-07-06T21:49:52.926268Z"
                },
                {
                    "start_time": "2020-07-06T21:49:57.698529Z",
                    "end_time": "2020-07-06T21:49:57.698569Z"
                },
                {
                    "start_time": "2020-07-06T21:50:01.462879Z",
                    "end_time": "2020-07-06T21:50:01.462942Z"
                }
            ]
        }
    ]
}
```
## Deployment

Django API is deployed on PythonAnywhere. [URL](http://bhuvneshgupta.pythonanywhere.com/)
