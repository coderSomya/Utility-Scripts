#!/bin/bash

# Function to find and delete node_modules directories
delete_node_modules() {
    # Find all node_modules directories and delete them
    find / -type d -name "node_modules" -prune -exec rm -rf '{}' +
}

# Call the function to delete node_modules directories
delete_node_modules

echo "All node_modules directories deleted."

