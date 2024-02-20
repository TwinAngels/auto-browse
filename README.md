# Automate navigation for POV and log generation

This script is designed to assist in various ways. Firstly, it aids in Point of View (POV) by automating the browsing process and therefore saves time that would have been spent on manual browsing. Secondly, it facilitates the collection of input and log data, which are essential in filling up the dashboard for a comprehensive view of the browsing process.

Furthermore, this script can be a valuable tool for customers wishing to perform stress tests on the Skyhigh web policy. Through automated and systematic navigation of specified URLs, the script can simulate substantial traffic and activity, providing valuable insights into the robustness and reliability of the web policy under stress conditions.

The script functions by systematically navigating through a list of specified URLs, eliminating the need for manual input. This guide has been designed to provide a step-by-step process to effectively set up and use the auto-browser script, streamlining your browsing process and enhancing your digital productivity.

# Steps

1. **Download the auto-browse script** - Begin by downloading the auto-browse script. This script contains the main code for automating the browsing process. After downloading, place the script in your C:/ drive. This location is often preferable as it is easily accessible and typically has sufficient storage space.
2. **Download ChromeDriver** - The auto-browser script works in conjunction with ChromeDriver, a separate component that enables the script to interface with the Chrome browser. Therefore, the next step involves downloading the latest version of ChromeDriver. Make sure to download the version compatible with your Chrome browser, and place it on the same folder as the script. (C:/AutoBrowse)
3. **Execute Install.bat** - Once ChromeDriver is downloaded, you need to execute the Install.bat file. This file is responsible for installing all the prerequisites needed for the auto-browser script to function smoothly. A simple double-click should suffice to run the file.
4. **Fill urls.txt** - Now that the script and its prerequisites are set up, the next step is to specify the URLs you wish to auto-browse. You can do this by filling the urls.txt file with your desired URLs. Alternatively, you can copy some or all of the URLs from the urls-full.txt file, if provided.
5. **Run Auto-navigate.bat** - With your URLs in place, you are now ready to run the Auto-navigate.bat file. This will initiate the auto-browsing process. Sit back and watch as the script seamlessly navigates through the list of URLs you provided.

## Recommendations

- **Shortcut on the Desktop** - For quick and easy access, it is recommended to create a shortcut to the auto-navigate file on your desktop. This way, you can initiate the auto-browsing process with a single click.
- **Schedule a Daily Run** - To maximize the benefits of the auto-browser script, consider scheduling a job that runs the script daily. This can be particularly useful for tasks such as daily website checks or routine data collection.
- **Validate Websites** - It is always a good practice to validate the websites you plan to auto-browse. You can use the [Domaincheck.py](http://domaincheck.py/) file to remove any non-existing websites from your list. This tool checks the validity of the URLs and ensures that your list only contains active and valid websites. This will result in the creation of the urls-validated.txt file, which you can use for error-free auto-browsing.
