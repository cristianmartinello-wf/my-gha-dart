open_prs = get_all_open_prs()
for pr in open_prs:
    requests.post(f"{RMCONSOLE_HOST}/api/v1/pull_requests/{pr.number}/set_automerge", json={"allowed": True})