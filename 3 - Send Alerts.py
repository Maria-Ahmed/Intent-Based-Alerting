import duckdb
import requests
from datetime import datetime, timedelta


def get_high_intent_contacts(connection):
  today = datetime(2024, 4, 30)
  fourteen_days_ago = (today - timedelta(days=14)).strftime("%Y-%m-%d")

  query= connection.sql("""
              SELECT 
    v.email
    FROM 
        crm.valid_emails v
    JOIN 
        crm.outreach_emails oe 
        ON v.email = oe."to"
    JOIN 
        (
            SELECT 
                "to", 
                MAX(sent_date_utc) AS max_sent_date_utc
            FROM 
                crm.outreach_emails
            GROUP BY 
                "to"
        ) max_oe 
        ON oe."to" = max_oe."to" AND oe.sent_date_utc = 
    max_oe.max_sent_date_utc
    WHERE 
        v.is_email_valid = TRUE AND oe.sent_date_utc <= ?;
          """, params = [fourteen_days_ago])
  return query

def send_alert_message(contacts):
  """
  Sends alert message to Business Development team for each contact.
  """

  subject = "High Buying Intent Contacts Alert"
  _from = "MariaAhmed"
  webhook_id = "88fac809-b756-4eea-baa7-6082bbf64e7e"

  message = "These contacts have shown high buying intent->    "
  message += ", ".join(contacts)
  message += f"  - Please reach out to these contacts at their email addresses.\n"

  payload = {
    "from": _from,
    "to": "biz-dev@taktile.com",
    "subject": subject,
    "message": message
  }

  # sending  request to webhook
  response = requests.post(f"https://webhook.site/{webhook_id}", json=payload) 
  if response.status_code==200:
    print("Posted successfully!")
  else:
    print("ERROR!")

if __name__ == "__main__":
  connection = duckdb.connect("data/db.duckdb")

  contacts = get_high_intent_contacts(connection=connection)
  send_alert_message(contacts=[contact[0] for contact in contacts.fetchall()])

  connection.close()

