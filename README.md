<div id="readme-top"></div>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h2 align="center">Schema API Validation</h2>

  <p align="center">
    Created by: Michael Montanaro
    <br />
    <br />
    <br />
    <a href="#usage">View Demo</a>
    ·
    <a href="https://github.com/montymi/SchemeAPITesting/issues">Report Bug</a>
    ·
    <a href="https://github.com/montymi/SchemaAPITesting/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#tasks">Tasks</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This repo is a walkthrough on how to validate schema files against API's via their server responses using Postman. The example is simple but highly applicable and easily modified to meet your use case. Following the steps below will get yoyou more familiar with Postman before you attempt to switch over to your own projects.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

The following will lead you through how to use the files in this repo to conduct the same testing in Postman for practice:

- Clone this repo (below uses HTTPS method):
```
git clone https://github.com/montymi/SchemaAPITesting.git
```
- Navigate into the directory and copy the contents of `postmanHTTPresponse.json`
- Go to [mocky.io](https://designer.mocky.io/), click `New Mock` and paste the contents of the json file into the HTTP Response Body section
- Change the expiration date of this mock HTTP server (if you would like)
- Click `GENERATE MY HTTP RESPONSE` and copy the url that is generated (will be used later so save it somewhere if necessary)
- Sign into your Postman account, it is completely free for individual use


That's it for the setup, go to [Usage](#usage) for next steps.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Below will take you through steps necessary to setup a testing environment and run the created tests. It is important to note that some of the techniques/steps below (ie. environment setup) are strictly good practice, but can be substituted for other methods. 

1. Create and name a workspace (ex. Schema Validation)
2. On the left side of the screen, click on `Environments`
3. Click `+`, name the environment (ie. `Live`)
4. In the variable column, write `url`
5. In the initial value column (and the current value column), paste the link to the created `mocky.io` site
6. In the top right, click `No Environment` and select the name of your environment in the drop down menu
7. On the left side of the screen, click `Collections`
8. Click the `+`, name the collection (ie. `Basic Schema`)
9. Create two new requests (ie. `PASSED Test` and `FAILED Test`)
10. In the `get` bar of both requests, type `{{url}}`
- Note: this can just be substituted with the `mocky.io` link
11. Click on the `Tests` tab and paste in the contents of the `postmanTesting.js` file that is in this directory
12. Based on desired outcome, change line 22 to be `failedSchema` or `passedSchema`
- Note: `failedSchema` includes a `test` parameter that is *required* and thus fails because it is not present in the HTTP response
13. Click on the main collection tag (ie. `Basic Schema`)
14. Click on the `Runs` tab and click `Run Collection`
15. Lastly, no need to change any settings, just click the `Run` button near the bottom of the page
- *IMPORTANT*: In order to import your own schema file, the link must be for the *raw* content not the general github page

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- STRUCTURE -->
## Structure

- README.md -> Walkthrough of testing procedure
- failed-schema.json -> schema validated against HTTP response that will FAIL because of added `test` parameter marked as *required*
- passed-schema.json -> schema validated against HTTP response that will PASS because the parameters match
- postmanHTTPResponse.json -> file whose contents are set to be the HTTP response by the `mocky` server
- postmanTesting.js -> file whose contents are pasted into the `Tests` section of a Postman request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- TASKS -->
## Tasks

By publicly displaying the to-do list of the project, users are able to see any feature that is nearing implementation. The list also allows new developers to quickly find potential tasks for them to complete which is an ideal way to familiarize them with the source code and to continue to make commits.

- [X] Emphasize 5.4% of projects section (speculation about what the observable differences would be if it were a higher figure)
- [X] Fix "Built With" logos section
- [X] Revision at the sentence level
- [X] Center architecture image
- [X] Add Author's Note
- [X] Fix some links
- [ ] Add beginner project to repository
- [ ] Change code examples to be example project

See the [open issues](https://github.com/montymi/ClearDocs/issues) for a full list of issues and proposed features.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are, in my opinion, the greatest part of OSS and are what will be the key to continuing the growth of the community. One of the main goals of this README is to facilitate contributions of potential developers. In this section, developers must be sure to lay out any coding styling choices that they may have so that the source code can remain as uniform as possible. One such project that has an immpressive contributions page is *htop* by [htop-dev](https://github.com/htop-dev/htop) who point all potential incoming contributors to their [style guide](https://github.com/htop-dev/htop/blob/main/docs/styleguide.md)

1. [Fork the Project](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. [Open a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

*Documentation must include a license section in which the type of license and a link or reference to the full license in the repository is given.*

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Michael Montanaro - [LinkedIn](https://www.linkedin.com/in/michael-montanaro/) - montanaro.m@northeastern.edu

Project Link: [https://github.com/montymi/ClearDocs](https://github.com/montymi/ClearDocs)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list any resources used or that may be helpful in understanding the project

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/montymi/ClearDocs.svg?style=for-the-badge
[contributors-url]: https://github.com/montymi/ClearDocs/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/montymi/ClearDocs.svg?style=for-the-badge
[forks-url]: https://github.com/montymi/ClearDocs/network/members
[stars-shield]: https://img.shields.io/github/stars/montymi/ClearDocs.svg?style=for-the-badge
[stars-url]: https://github.com/montymi/ClearDocs/stargazers
[issues-shield]: https://img.shields.io/github/issues/montymi/ClearDocs.svg?style=for-the-badge
[issues-url]: https://github.com/montymi/ClearDocs/issues
[license-shield]: https://img.shields.io/github/license/montymi/ClearDocs.svg?style=for-the-badge
[license-url]: https://github.com/montymi/ClearDocs/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/michael-montanaro
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
