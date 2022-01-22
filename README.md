# Back-end
# Version
> python: 3.9.5
> 
> django: 3.0.5
# Run
> python3 manage.py runserver 0:8000
# API
> ## GET /parkinfo
> ### Request Data
> ```
> Query params:
>   search: <value>
>   latitude <value>
>   longitude <value>>
> ```
> ### Response Data
> ```
> body:
> {
>   "total": {
>     "value": <int>,
>     "relation": eq,
>   }
>   "max_score": <double>,
>   "hits": [
>     {
>       Information about Park 
>     },
>     {
>     }
>   ]
> }
> ```
