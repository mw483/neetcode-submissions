class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for e in emails:
            unique_emails.add(e.split("@", 1)[0].replace(".", "").split("+", 1)[0] + e.split("@", 1)[1])
        return len(unique_emails)