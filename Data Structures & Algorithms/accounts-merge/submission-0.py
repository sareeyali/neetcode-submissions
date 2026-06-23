class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict

        # Union-Find with path compression
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # Step 1: Union emails, track names
        email_to_name = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                email_to_name[email] = name
                union(first_email, email)

        # Step 2: Group by root
        groups = defaultdict(list)
        for email in email_to_name:
            groups[find(email)].append(email)

        # Step 3: Format output
        return [[email_to_name[root]] + sorted(emails)
                for root, emails in groups.items()]