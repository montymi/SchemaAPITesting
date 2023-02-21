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
    Created by: [Michael Montanaro](https://github.com/montymi)
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

- *README.md* -> Walkthrough of testing procedure
- *failed-schema.json* -> schema validated against HTTP response that will FAIL because of added `test` parameter marked as *required*
- *passed-schema.json* -> schema validated against HTTP response that will PASS because the parameters match
- *postmanHTTPResponse.json* -> file whose contents are set to be the HTTP response by the `mocky` server
- *postmanTesting.js* -> file whose contents are pasted into the `Tests` section of a Postman request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are, in my opinion, the greatest part of OSS and are what will be the key to continuing the growth of the community. One of the main goals of this README is to facilitate contributions of potential developers. In this section, developers must be sure to lay out any coding styling choices that they may have so that the source code can remain as uniform as possible. One such project that has an immpressive contributions page is *htop* by [htop-dev](https://github.com/htop-dev/htop) who point all potential incoming contributors to their [style guide](https://github.com/htop-dev/htop/blob/main/docs/styleguide.md)

1. [Fork the Project](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
2. Create your Feature Branch (`git checkout -b feature/Example`)
3. Commit your Changes (`git commit -m 'Adding example feature'`)
4. Push to the Branch (`git push origin feature/Example`)
5. [Open a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU General Public License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Michael Montanaro - [LinkedIn](https://www.linkedin.com/in/michael-montanaro/) - [GitHub](https://github.com/montymi) - [Email](mcmontanaro01@gmail.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Valentina Despa](https://www.youtube.com/watch?v=P_So0vpNJCQ&t=211s&ab_channel=ValentinDespa)
* [Postman](https://learning.postman.com/docs/writing-scripts/test-scripts/)
* [OpenAPI Spec v3.1.0](https://spec.openapis.org/oas/v3.1.0)
* [Mocky](https://mocky.io)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/montymi/SchemaAPITesting.svg?style=for-the-badge
[contributors-url]: https://github.com/montymi/SchemaAPITesting/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/montymi/SchemaAPITesting.svg?style=for-the-badge
[forks-url]: https://github.com/montymi/SchemaAPITesting/network/members
[stars-shield]: https://img.shields.io/github/stars/montymi/SchemaAPITesting.svg?style=for-the-badge
[stars-url]: https://github.com/montymi/SchemaAPITesting/stargazers
[issues-shield]: https://img.shields.io/github/issues/montymi/SchemaAPITesting.svg?style=for-the-badge
[issues-url]: https://github.com/montymi/SchemaAPITesting/issues
[license-shield]: https://img.shields.io/github/license/montymi/SchemaAPITesting.svg?style=for-the-badge
[license-url]: https://github.com/montymi/SchemaAPITesting/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/michael-montanaro
