# Recursive function to remove node_modules directories
function Remove-NodeModules {
    param (
        [string]$path
    )

    # Get all directories in the current path
    $directories = Get-ChildItem -Path $path -Directory -ErrorAction SilentlyContinue

    # Loop through each directory
    foreach ($dir in $directories) {
        # If directory name is node_modules, delete it
        if ($dir.Name -eq "node_modules") {
            Remove-Item -Path $dir.FullName -Recurse -Force
            Write-Host "Removed $($dir.FullName)"
        }
        else {
            # If not node_modules, recursively call Remove-NodeModules on it
            Remove-NodeModules -path $dir.FullName
        }
    }
}

# Start the removal process from the root directory (change it to your desired directory if needed)
Remove-NodeModules -path "C:\"

