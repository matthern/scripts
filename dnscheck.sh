#!/bin/bash
#Usage: put DNS in first 2 arguments 
# not completed tested

# Set the expected DNS servers
EXPECTED_DNS=("$1" "$2")

# Get the current DNS server from systemd-resolved
CURRENT_DNS=$(systemd-resolve --status | grep 'DNS Servers' | awk '{print $NF}')

# Check if the current DNS is in the list of expected DNS servers
if [[ " ${EXPECTED_DNS[@]} " =~ " ${CURRENT_DNS} " ]]; then
    echo "DNS server is set to $CURRENT_DNS. No action needed."
else
    echo "DNS server is not set to one of the expected values. Restarting systemd-resolved..."

    # Restart systemd-resolved
    systemctl restart systemd-resolved

    # Check if systemd-resolved has been restarted successfully
    if [[ "$(systemd-resolve --status | grep 'DNS Servers' | awk '{print $NF}')" == "${EXPECTED_DNS[0]}" || "$(systemd-resolve --status | grep 'DNS Servers' | awk '{print $NF}')" == "${EXPECTED_DNS[1]}" ]]; then
        echo "systemd-resolved restarted successfully. DNS is now set to ${EXPECTED_DNS[@]}."
    else
        echo "Failed to restart systemd-resolved. Please check the logs for more information."
    fi
fi
