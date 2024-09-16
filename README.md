### Fitmatrix

Fitness Meets Innovation

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app fitmatrix
```

### Workspace

<p align="center">
  <img width="400" height="250" src="fitmatrix/public/documentation/images/workspace1.png" alt="Workspace 1" />
  <img width="400" height="250" src="fitmatrix/public/documentation/images/workspace2.png" alt="Workspace 2" />
</p>

<p align="center">
  <img width="400" height="250" src="fitmatrix/public/documentation/images/workspace3.png" alt="Workspace 3" />
  <img width="400" height="250" src="fitmatrix/public/documentation/images/workspace4.png" alt="Workspace 4" />
</p>







### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/fitmatrix
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade


### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
