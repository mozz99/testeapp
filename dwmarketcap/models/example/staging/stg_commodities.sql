-- import

with source as (
    select
        "datetime_request",
        "api_timestamp",
        "Close",
        "simbolo",
        "moeda"
    from 
        {{ source ('dbsalesaovivo_qckj', 'commodities') }}
),

renamed as (

    select
        cast("datetime_request" as date) as data,
        "api_timestamp" as api_timestamp,
        "simbolo" as simbolo,
        "Close" as fechamento,
        "moeda" as moeda
    from
        source
    limit 5
)

select * from renamed