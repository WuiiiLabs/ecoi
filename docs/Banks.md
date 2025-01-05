# Banks
```py
from core.economy import banks
```
## Functions

- Use to invest and then they bring up profit
- Tie up with group rep. and perform operations for the group
- Prviding services like credit cards, debit cards, savings account 
- is it for co-operative development measures?
- for funding long term projects which is capital intensive
- currency exchange transaction for banks

## CURD+ Operations
### Bank Creation
```py
bank = banks.createBank(
    name: str,
    logo: str,
    owner_id: str,
    group_id: str,
    address: str,
    contact: str,
    site: str,
    gmail: str,
    description: str,
    openHours: (datetime, datetime),
    investment: List[dict],    
)

# the investment looks something like this
[
    {
        "amount": int,
        "moe_id": str,
    },
    # others
]
```
### Bank Setup
```py
bank.setup(
    gsupport: List[str], # group_ids supporting dictionaries
    cooperative: bool,
    user_schema: dict,
    adm_schema: dict,
    projects: list,
)
```
### Bank Update
```py
bank.update(
    name: str,
    logo: str,
    address: str,
    contact: str,
    site: str,
    gmail: str,
    description: str,
    openHours: (datetime, datetime),
    investment: List[dict],
    **kwargs,
)
```
### Bank Read
```py
bank.read()
```
### Bank Upgrade
```py
bank.upgrade(...)
``` 
### Bank Delete
```py
bank.delete()
```

### Branch Operations
```py
bank.createBranch(...)
bank.updateBranch(...)
bank.readBranch(...)
bank.deleteBranch(...)
```

## Currency Exchange
```py
bank.currencyExchange(
    from_moe_id: str,
    to_moe_id: str,
    amount: int,
) -> [to_moe]*amount
``` 