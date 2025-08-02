<a id="readme-top"></a>

<br />
<div align="center">
  <a href="https://github.com/larstel/minimalistFramework">
    <img src="static/icon.svg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">minimalist.build</h3>

<p align="center">
    A lightweight framework for building web frontends, designed to minimize boilerplate code and repetitive tasks while leaving you in control of all key decisions.
    <br />
    <a href="https://github.com/larstel/minimalistFramework"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://grammaticus.io">View Demo</a>
    ·
    <a href="https://github.com/larstel/minimalistFramework/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/larstel/minimalistFramework/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
# About The Project

This project offers a straightforward framework for building web frontends efficiently, with less overhead compared to larger frameworks.

In a nutshell, you create files in a specific structure, and the framework takes care of building an entire website from them.

## Features
* handles repetitive code such as headers, footers and navigation
* uses localization files to translate pages into different languages
* helps organize the project structure
* automatically applies various SEO strategies
* provides a ready-to-deploy directory

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

# Getting Started

1. Install Python:
   ```sh
   apt-get install python
   ```
2. Create project directory:
   ```sh
   mkdir "directory-name"
   ```
3. Create a buildConfig.json file in your project's root directory:
    ```sh
    touch buildConfig.json
    ```
4. Create a template.html file in your project's root directory:
    ```sh
    touch template.html
    ```
5. Add all custom files like styles, images etc. under 'additionalFilesForServer/':
    ```sh
    mkdir additionalFilesForServer
    ```
6. Add a content folder:
    ```sh
    mkdir contentTemplates
    ```
7. (optional) add a content sub folder:
    ```sh
    cd contentTemplates
    mkdir topic
    ```
8. Add a localization.json file to your project's content folder:
    ```sh
    (optional) cd topic
    touch localization.json
    ```
9. If your project isn't already a Git repository, initialize it:
    ```sh
    cd ../../
    git init
    ```
10. Clone the repository as a submodule in your project's directory:
    ```sh
    git submodule add https://github.com/larstel/minimalistFramework.git
    ```
11. Switch to the directory the submodule is located at:
    ```sh
    cd minimalistFramework
    ```
12. Install the required Python packages:
    ```sh
    pip3 install -r requirements.txt
    ```
13. Fill the files, like in the following section described
   

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## template.html
The template html is the template every component is using as ground work.

### builder content tag
| tag         | example          | description          |
| -------------------- | ----------------------------- | ---------------------------------------- |
| `<builder-content></builder-content>` |           |  copy the components content into this positon       |
| `<builder-title></builder-title>`     | `<title><builder-title></builder-title></title>` | gets the title defined in the components localization file |
| `<builder-header-tags></builder-header-tags>` |           | enable the feature of noindex config in buildConfig.json        |
| `<builder-header></builder-header>` |           |  get header title defined in buildConfig.json       |
| `<builder-sub-header></builder-sub-header>` |           |         |
| `<html lang="builder-content-language"></html>` |           |         |
| `<meta name="description" content="builder-content-description">` |           |         |
| `<meta name="keywords" content="builder-content-keywords">` |           |         |

## buildConfig.json (mandatory)<a id="buildConfig"></a>

### available configs (currently all mandatory):


| config               | example                       | description                              |
| -------------------- | ----------------------------- | ---------------------------------------- |
| contentTemplatesPath | "contentTemplates/"           | the directory where all pages are        |
| content              | "topic" or ""                 | the sub directory where all pages are        |
| availableLanguages   | ["en", "de"]                  | all available languages of the website   |
| mainLanguage         | "en"                          | the main language the website is developed for   |
| navigationBlacklist  | "index.html", "imprint.html", "privacy.html", "error.html" | all sites which should not appear in nav. It also adds a meta tag which stops search engines to follow and index the pages. |
| noindex  | "imprint.html", "privacy.html", "error.html" | all sites which should not appear in search engines. |
| noNavigation  | "imprint.html", "privacy.html", "error.html" | all sites which should not have a navigation. |
| iconPath             | "static/icon.svg"             | the path where the icon exists           |
| header               | "Title"                       | the header at the top of all pages       |
| subHeader            | "sub-title"                   | the sub header at the top of all pages   |
| copyrightSince            | "2021"                   | since when the copyright exists   |
| domain            | "github.com"                   | the domain the website should be use   |
| hasFooter            | true | false                  | if a footer should be generated   |

### Example:

~~~~
{
    "contentTemplatesPath": "contentTemplates/",
    "content": [""],
    "availableLanguages": ["en"],
    "mainLanguage": "en",
    "navigationBlacklist": ["imprint.html", "privacy.html", "error.html"],
    "noindex": ["imprint.html", "privacy.html", "error.html"],
    "noNavigation": ["index.html"],
    "iconPath": "static/icon.svg",
    "header": "Title",
    "subHeader": "sub-title",
    "copyrightSince": "2021",
    "domain": "github.com",
    "hasFooter": "false"
}
~~~~

## custom.css (mandatory)

- for implementing custom css classes

## Localization
### localization.json - general localization (mandatory)
### Example:
~~~~
{
    "language": {
        "de": "englisch",
        "en": "english"
    }
}
~~~~

## component localization


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
    },
    "title": {
        "de": "",
        "en": ""
    }
}
~~~~

## contentTemplates

insert all pages/components here



<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Usage
To build the static html files:
```sh
python3 build.py
```
To start a live server and automatic page building:
```sh
python3 serve.py
```

<!-- ROADMAP -->

# Roadmap

See the [open issues](https://github.com/larstel/minimalistFramework/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

# Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

# License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
