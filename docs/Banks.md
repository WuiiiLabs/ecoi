# Banks
```py
from core.economy.banks import Bank
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
bank = Bank.createBank(
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
```py
bank.createCard(...)
bank.updateCard(...)
bank.readCard(...)
bank.deleteCard(...)
```

## Bank Processes
```py
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
```

## Bank Config
```py
bank.setConfig(...)
bank.updateConfig(...)
```

## Bank Accounts
```py
acc = bank.createAccount(...)
acc_id = acc.id

bank.getAccount(acc_id, ...)
bank.getAccounts(...)

bank.updateAccounts(...)
bank.deleteAccounts(...)
bank.freezeAccounts(...)
```

## Account Cards
```py
card = acc.createCard(...)
card.updateCard(...)
card.read(...)
card.delete()
```

## Customers
```py
custModel = Bank.modelCustomer(...)
custModel.update(...)
custModel.read(...)
custModel.delete()

cust = Bank.createCustomer(...)
cust.modelUpdate(...)
cust.read(...)
cust.delete()
```

## Department
```py
dept = Bank.createDept(...)
dept.update(...)
dept.read(...)
dept.delete(...)
```

## Tickets
```py
Bank.setTicketRole(...) # name and perms
Bank.updateTicketRole(...)
Bank.readTicketRole(...)
Bank.delTicketRole(...)

ticket = Bank.createTicket(...)
ticket.open(...)
ticket.close(...)
ticket.report(...)
ticket.assign(...)
ticket.update(...)
ticket.read(...)
ticket.delete()
```

## Bank Roles
```py
role = Bank.createRole(...)
role.update(...)
role.read(...)
role.setPermissions(...)
role.updatePermissions(...)
role.addEmployee(...)
role.updateEmployee(...)
role.removeEmployee(...)
role.delete()
```

## Currency Exchange
```py
bank.currencyExchange(
    from_moe_id: str,
    to_moe_id: str,
    amount: int,
) -> [to_moe]*amount
``` 