# Helpful Terminal Commands

## Basic Directory Navigation and File Management

### Print the Working Directory

`pwd` is used to print the current working directory.

```bash
pwd # Print the absolute path to the current working directory
```

### List Files

`ls` is used to list the files in a given directory.

```bash
ls # List files in the current directory
ls -a # List all files in the current directory, including hidden files
ls -l # List files in the current directory with long format
ls -la # List all files in the current directory with long format, including hidden files
ls -R # List all files in the current directory and all subdirectories recursively
ls path_to_directory # List files at a certain path
```

### Change Directory

`cd` is used to change the current directory. It can be used to move up or down the directory tree.

```bash
cd .. # Move up (back) one directory
cd ../.. # Move up two directories
cd ~ # Move to the home directory
cd / # Move to the root directory
cd subdirectory_name_here # Move to a subdirectory of the current directory
```

### Make a Directory

`mkdir` is used to create a new directory.

```bash
mkdir directory_name_here # Create a new directory in the current directory
mkdir path_to_directory/directory_name_here # Create a new directory at a certain path
```

### Remove a Directory

`rmdir` is used to remove a directory, but only if it is empty.

```bash
rmdir directory_name_here # Remove a directory in the current directory
rmdir path_to_directory/directory_name_here # Remove a directory at a certain path
```

### Create a File

`touch` is used to create a new file or update the timestamp of an existing file.

```bash
touch file_name_here # Create a new file in the current directory
touch path_to_directory/file_name_here # Create a new file at a certain path
touch -a file_name_here # Update the access timestamp of a file
touch -m file_name_here # Update the modification timestamp of a file
touch -t datetime_number_sequence file_name_here # Set the timestamp of a file to a specific datetime numeric sequence
```

### Remove a File or Directory

`rm` is used to remove a file.

```bash
rm file_name_here # Remove a file in the current directory
rm path_to_directory/file_name_here # Remove a file at a certain path
rm -r directory_name_here # Remove an empty directory recursively
rm -rf directory_name_here # Remove a directory in the current directory recursively, even if it is not empty
```

### Move a File or Directory

`mv` is used to move a file or directory. This is also used to rename a file or directory.

```bash
mv file_name_here new_file_name_here # Rename a file in the current directory
mv path_to_directory/file_name_here new_file_path_here # Move a file to a new location
mv directory_name_here new_directory_name_here # Rename a directory in the current directory (same as you would with a file)
mv path_to_directory/directory_name_here new_directory_path_here # Move a directory to a new location (same as you would with a file)
```

### Copy a File or Directory

`cp` is used to copy a file or directory.

```bash
cp file_name_here new_file_name_here # Copy a file in the current directory
cp path_to_directory/file_name_here new_file_path_here # Copy a file to a new location
cp -R directory_name_here new_directory_name_here # Copy a directory in the current directory (same as you would with a file)
cp -R path_to_directory/directory_name_here new_directory_path_here # Copy a directory to a new location (same as you would with a file)
```

## Compressing, Extracting, and Archiving Files

### Zip a File or Directory

`zip` is used to zip a file or directory.

```bash
zip output_file_name_here.zip file_name_here # Zip a file in the current directory
zip output_file_name_here.zip path_to_directory/file_name_here # Zip a file at a certain path
zip output_file_name_here.zip directory_name_here # Zip a directory in the current directory
zip output_file_name_here.zip path_to_directory/directory_name_here # Zip a directory at a certain path
zip -r output_file_name_here.zip directory_name_here # Zip a directory in the current directory recursively
zip -r output_file_name_here.zip path_to_directory/directory_name_here # Zip a directory at a certain path recursively
zip -r -X output_file_name_here.zip directory_name_here # Zip a directory in the current directory recursively, excluding hidden files
zip -r -X output_file_name_here.zip path_to_directory/directory_name_here # Zip a directory at a certain path recursively, excluding hidden files
```

### Unzip a Zip File

`unzip` is used to unzip a zip file.

```bash
unzip file_name_here.zip # Unzip a zip file in the current directory
unzip path_to_directory/file_name_here.zip # Unzip a zip file at a certain path
```

## File Viewing in the Terminal

### View an Entire File in the Terminal

`cat` is used to view the contents of a file.

```bash
cat file_name_here # View the contents of a file in the current directory
cat path_to_directory/file_name_here # View the contents of a file at a certain path
cat -n file_name_here # View the contents of a file in the current directory with line numbers
cat -b file_name_here # View the contents of a file in the current directory with non-blank line numbers
```

### View the First Few Lines of a File

`head` is used to view the first few lines of a file.

```bash
head file_name_here # View the first 10 lines of a file in the current directory
head -n number_of_lines_to_view file_name_here # View the first n lines of a file in the current directory
```

### View the Last Few Lines of a File

`tail` is used to view the last few lines of a file.

```bash
tail file_name_here # View the last 10 lines of a file in the current directory
tail -n number_of_lines_to_view file_name_here # View the last n lines of a file in the current directory
```
