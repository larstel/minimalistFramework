<a id="readme-top"></a>

<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url] 
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->

<!-- PROJECT LOGO -->

<br />
<div align="center">
  <a href="https://github.com/larstel/minimalist">
    <img src="static/icon.svg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Minimalist Framework</h3>

<p align="center">
    A lightweight framework for building web frontends, designed to minimize boilerplate code and repetitive tasks while leaving you in control of all key decisions. Developed in Python.
    <br />
    <a href="https://github.com/larstel/minimalist"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/larstel/minimalist">View Demo</a>
    ·
    <a href="https://github.com/larstel/minimalist/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/larstel/minimalist/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <!-- <li><a href="#installation">Installation</a></li> -->
      </ul>
    </li>
    <!-- <li><a href="#usage">Usage</a></li> -->
    <li><a href="#roadmap">Roadmap</a></li>
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This project offers a straightforward framework for building web frontends efficiently, with less overhead compared to larger frameworks.

In a nutshell, you create files in a specific structure, and the framework takes care of building an entire website from them.

### Features
* Eliminates duplicated code
  * Automatically generates navigation and header and inserts it on every page
  * Write pages in a single spoken language, and the framework assists with localization
* Helps organize your project structure
* Automatically manages URL structure
  * Supports multiple spoken languages
  * Organizes URLs for all pages
* Enhances your site’s SEO by implementing various strategies automatically
* Simplifies localization
* Builds the project and provides a ready-to-deploy directory

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Installation



1. If your project isn't already a Git repository, initialize it:
    ```sh
    git init
    ```
2. Clone the repository as a submodule in your project's root directory:
    ```sh
    git submodule add https://github.com/larstel/minimalist.git
    ```
3. Install Python:
   ```sh
   sudo apt-get install python
   ```
4. Install the required Python packages:
   ```sh
   pip3 install -r requirements.txt
   ```
5. Create a buildConfig.json file in your project's root directory with the specified content:
    ```sh
    touch buildConfig.json
    ```
6. Add a custom.css file to your project's root directory:
    ```sh
    touch custom.css
    ```
7. Add a localization.json file to your project's content folder:
    ```sh
    touch localization.json
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

#### buildConfig.json (mandatory)<a id="buildConfig"></a>

##### available configs (currently all mandatory):


| config               | example                       | description                              |
| -------------------- | ----------------------------- | ---------------------------------------- |
| contentTemplatesPath | "contentTemplates/"           | the directory where all pages are        |
| availableLanguages   | ["en", "de"]                  | all available languages of the website   |
| navigationBlacklist  | "imprint", "privacy", "error" | all sites which should not appear in nav |
| iconPath             | "static/icon.svg"             | the path where the icon exists           |
| header               | "Title"                       | the header at the top of all pages       |
| subHeader            | "sub-title"                   | the sub header at the top of all pages   |

###### Example:

~~~~
{
    "contentTemplatesPath": "contentTemplates/",
    "availableLanguages": ["en"],
    "navigationBlacklist": [],
    "iconPath": "static/icon.svg",
    "header": "Title",
    "subHeader": "sub-title"
}
~~~~

#### custom.css (mandatory)

- for implementing custom css classes

#### Localization
##### general localization (mandatory)
###### Example:
~~~~
{
    "language": {
        "de": "englisch",
        "en": "english"
    }
}
~~~~

##### component localization


- each content template needs its own localization file
- naming: "index-of-menu-entry"_"filename"_localization.json

File must at least contain the following content:

~~~~
{
    "keywords": {
        "de": "",
        "en": ""
    },
    "description": {
        "de": "",
        "en": ""
    },
    "filename": {
        "de": "",
        "en": ""
    }
}
~~~~

<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [ ] enable the creation of multiple HTML templates for the entire project

See the [open issues](https://github.com/larstel/minimalist/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ### Top contributors:

<a href="https://github.com/larstel/minimalist/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=larstel/minimalist" alt="contrib.rocks image" />
</a> -->

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

<!-- ACKNOWLEDGMENTS -->

<!-- ## Acknowledgments

* []()
* []()
* []() -->

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- MARKDOWN LINKS & IMAGES -->

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
