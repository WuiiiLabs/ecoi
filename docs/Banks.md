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

bank.setup(
    gsupport: List[str], # group_ids supporting dictionaries
    cooperative: bool,
    user_schema: dict,
    adm_schema: dict,
    projects: list,
)

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

bank.read(
    format = Literal['dict', 'bson'],
    print_console = Literal[True, False],
    filter: dict,
    query_vars: list = None,
    limit: int=10,
)

bank.upgrade(...)

bank.delete()
```

### Branch 
#### CURD+ Operations
```py
bank.createBranch(...)
bank..updateBranch(...)
bank.readBranch(...)
bank.updateBranch(...)
bank.deleteBranch(...)
```

## Cards
bank.createCard(...)
bank.updateCard(...)
bank.readCard(...)
bank.deleteCard(...)

## Bank Processes
process = bank.createProcess(...)
process_id = process.id

process.start(...)
process.automate(...)
process.bind(...)
process.update(...)
process.restart(...)
process.delete()

process.createSubProcess(...)
process.getSubProcesses(...)
process.killSubProcesses(...)

## Bank Config
bank.setConfig(...)
bank.updateConfig(...)

## Bank Accounts
acc = bank.createAccount(...)
acc_id = acc.id

bank.getAccount(acc_id, ...)
bank.getAccounts(...)

bank.updateAccounts(...)
bank.deleteAccounts(...)
bank.freezeAccounts(...)

## Account Cards
card = acc.createCard(...)

acc.updateCard(...)


## Currency Exchange
```py
bank.currencyExchange(
    from_moe_id: str,
    to_moe_id: str,
    amount: int,
) -> [to_moe]*amount
``` 