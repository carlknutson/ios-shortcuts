from datetime import datetime
import json
import os
import requests
import sys

ynab_api_url = 'https://api.ynab.com/v1'
ynab_token = os.environ['ynab_token']
ynab_budget_name = os.environ['ynab_budget_name']

def add_transaction(account_name, message):
    budgets = requests.get(url=f'{ynab_api_url}/budgets', params={'include_accounts': 'true'}, headers={'Authorization': f'Bearer {ynab_token}'}).json()['data']['budgets']
    budget_id = None
    account_id = None
    for budget in budgets:
        if budget['name'] == ynab_budget_name:
            budget_id = budget['id']
            for account in budget['accounts']:
                if account['name'] == account_name:
                    account_id = account['id']
    
    if not account_id:
        print(f'No account found with name {account_name}.')
        return
    
    transaction = {
        'transaction': {
            'account_id': account_id,
            'memo': message,
            'date': f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day}',
            'amount': 0,
            'cleared': 'uncleared',
            'approved': False,
        }
    }

    response = requests.post(url=f'{ynab_api_url}/budgets/{budget_id}/transactions', json=transaction, headers={'Authorization': f'Bearer {ynab_token}'})
    response.raise_for_status

    print(transaction)
    print(response)

def get_accounts():
    accounts = []

    budgets = requests.get(url=f'{ynab_api_url}/budgets', params={'include_accounts': 'true'}, headers={'Authorization': f'Bearer {ynab_token}'}).json()['data']['budgets']
    for budget in budgets:
        if budget['name'] == ynab_budget_name:
            for account in budget['accounts']:
                if not (account['closed'] or account['deleted']):
                    accounts.append(account['name'])
    print(accounts)

def get_payees():
    payees = []

    budgets = requests.get(url=f'{ynab_api_url}/budgets', headers={'Authorization': f'Bearer {ynab_token}'}).json()['data']['budgets']    
    for budget in budgets:
        if budget['name'] == ynab_budget_name:
            response = requests.get(url=f'{ynab_api_url}/budgets/{budget["id"]}/payees', headers={'Authorization': f'Bearer {ynab_token}'}).json()['data']['payees']

            for payee in response:
                if not (payee['deleted'] or payee['transfer_account_id']):
                    payees.append(payee['name'])
    return payees

def main():
    try:
        action = sys.argv[1]
    except IndexError:
        print('An action parameter, must be provided.')
        return

    if action == 'add_transaction':
        try:
            add_transaction(account_name=sys.argv[2], message=sys.argv[3])
        except IndexError:
            print(f'Action: {action}, requires an account and message')
    elif action == 'get_accounts':
        get_accounts()
    else:
        print(f'Action: {action}, is not implemented.')

if __name__ == "__main__":
    main()
