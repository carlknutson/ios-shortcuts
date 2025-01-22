## SMS to YNAB

#### Download [link](https://www.icloud.com/shortcuts/1a0ff302e4b54c33a80a897548ac23bc)

YNAB users may prefer not to link their bank accounts due to privacy or security concerns, yet still desire a quick and efficient way to track transactions. This iOS Shortcut bridges the gap by processing SMS credit card alerts to create transactions in YNAB almost instantly. By leveraging the details from these alerts, the shortcut populates the memo field in YNAB with the SMS message, making it easy to fill out the payee, amount, and category fields while keeping your account details secure and private.

## Getting Started

1. [a-Shell](https://apps.apple.com/us/app/a-shell/id1473805438) installed and configured on iPhone
1. **Enable SMS Notifications for Transactions**: Set up transaction notifications for all the accounts you want to track.
1. **Setup YNAB Config**: The SMS to YNAB shortcut relies on an additional shortcut called `Get Config` to manage environment variables and configurations. [Download the Get Config](https://www.icloud.com/shortcuts/d004d3c2b5f54ac0b3a6945ae753475c) shortcut and customize its configuration dictionary with the following properties:
    * `ynab_token`: Your YNAB personal access token (create one at YNAB API - Personal Access Tokens).
    * `ynab_budget`: The name of your YNAB budget.
    * `ynab_single_card`: A dictionary where the key is the SMS number sending the alerts, and the value is the corresponding payee in YNAB.
    * `ynab_multi_card`: A dictionary for handling multiple cards from the same institution. The key is the SMS number, and the value is another dictionary where the keys are the last 4 digits of the card, and the values are the corresponding payees in YNAB.
    * `alert_unapproved_count`: When set, specifies alerting conditions based on unapproved transactions across all accounts for the budget. This is evaluated after each transaction processed by the SMS message automation. Requirement for `alert_via_notification` and `alert_via_notification` functionality.
    * `alert_via_notification`: If set, will trigger a notification if unapproved transactions are equal or greater than `alert_unapproved_count`.
    * `alert_via_reminders`: Specify a Reminders list name if you want a reminder created when the unapproved count is met.
1. **Set Up Automation**: Create an automation on your iPhone to trigger the SMS to YNAB shortcut whenever you receive an SMS containing the `$` symbol. The shortcut will only add a transaction to YNAB if the sender address matches an entry in either `ynab_single_card` or `ynab_multi_card`.
