


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About Viewfinder</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About Viewfinder

Viewfinder is a user-friendly tool designed to simplify the analysis and visualization of CSV and Excel datasets. With an intuitive drag-and-drop interface, it offers a comprehensive overview, detailed statistics, and visualizations to help you understand your dataset quickly, the names comes from the viewfinder of cameras where you can get a quick preview useful information before taking the pic, in the same sense Viewfinder aims to help you get a quick preview of your dataset without having to load it on a jupiter notebook or other similar tool.

### Key Features:

- **Easy Import**: 
Drag and drop CSV or Excel files.
- **Data Overview**: 
Quick summary of columns, types, missing values, and sample data.
- **Statistics**: 
Descriptive stats for numerical columns. 
- **Visualizations**: 
Generate histograms to visualize data distributions.
- **Export**: 
Export data overview and statistics to Excel.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With:
- **Python** 

![Python](https://www.python.org/static/img/python-logo@2x.png?width=100)

- **PyQt5** 

![Qt logo](https://www.qt.io/hs-fs/hubfs/Qt-logo-neon_900px.png?width=100) 

- **Pandas** 

![Pandas](https://pandas.pydata.org/static/img/pandas.svg?width=100)
- **Matplotlib**

![MAtplotlib](https://matplotlib.org/stable/_static/logo_light.svg?width=100)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* Make sure to have python 3.12 installed.
*(having a venv to run viewfinder is a bit optional, its generally a good practice to keep venvs for projects to prevent littering your local python install, but you be you, if you want to install the requirements.txt directly on your local python config feel free to do so as well)*


* set up a python virtual enviroment:
  ```sh
   python -m venv venv
  ```
* activate the virtual enviroment using: 
* -On MacOs & Linux:
  ```sh
   source venv/bin/activate 
  ```

* -On Windows using CMD:
  
  ```sh
   .\venv\Scripts\activate.bat
  ```

### Installation

To install and set up Viewfinder, first ensure you have Python installed on your system. Clone the repository, navigate to the project directory, and install the required dependencies using pip. You can then run the application by executing the main script. Below are the step-by-step instructions:

1. Clone the repo
  ```sh
   git clone https://github.com/your_username_/Project-Name.git
  ```

2. install the dependencies using the requirements.txt file:
  ```sh
   pip install -r requirements.txt
  ```

3. Run the -main.py- file:
  ```sh
   Python main.py
  ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage


Just drag and drop your .csv or .xslx file on the window and see a quick preview of your dataset.



<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such a fantastic place to learn, inspire, and create. Any contributions you make to improve Viewfinder are **greatly appreciated**.

If you have suggestions for enhancements or new features, please fork the repository and create a pull request. You can also open an issue with the tag "enhancement". 
Don't forget to **give the project a star** if you like it!
Thanks again for your support!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- CONTACT -->
## Contact

Guillermo Taly 
opensource@guillermotaly.com

Project Link
 [https://github.com/Talyght/viewfinder](https://github.com/Talyght/viewfinder)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
### Resources

* [PyQt5 Reference Guide](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
* [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
* [Matplotlib Documentation](https://matplotlib.org/stable/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
