# SAS Open Source Contributor Handbook
Contributing to open source projects from SAS Institute Inc.

## Welcome, contributors
SAS is the founder and future of analytics.
When you contribute to SAS's open source projects, you'll build tools that help the people across the world make better decisions, faster.

## Where to start
[SAS Software](https://github.com/sassoftware) on GitHub is home to more than 200 open source projects from SAS.
Here you'll find open projects, plugins, examples, and other resources for extending and integrating SAS's powerful tools with open source languages and frameworks.
Browse the [project gallery](https://sassoftware.github.io/) to get started.

## Read the guidelines
If a [SAS open source project](https://sassoftware.github.io/) is accepting contributions, the project repository will contain a `CONTRIBUTING.md` file.
Read that file carefully.
It will contain important instructions for contributing to the project.
It might also offer details about the project's development and code review processes.
When you understand (and follow) these guidelines, you'll increase the likelihood that project maintainers will accept your contributions.

## Sign your work
Everyone contributing to SAS projects must sign [SAS's standard contributor agreement](https://github.com/sassoftware/.github/blob/main/ContributorAgreement.txt), which is built on the [Developer Certificate of Origin](https://developercertificate.org/).
To comply with the agreement and attest to your right to offer your contribution to a SAS project, simply add the following line to your commits:

```
Signed-off-by: Firstname Lastname <user@mail.com>
```

For example:

```
Signed-off-by: Random J Developer <random@developer.example.org>
```

You can add this line to your commits with this command:

```
git commit -s
```

SAS uses the [DCO app](https://github.com/apps/dco) to scan all commits in incoming pull requests and confirm this sign-off.
The app will alert you if your commits aren't properly signed-off.
It will also offer instructions for remediating the issue and providing proper sign-off.
SAS project maintainers won't merge your commit unless you've added proper sign-off.

## Submit for review
Each of SAS's open source projects has its own team of maintainers at SAS.
Each one therefore has its own set of code conventions and review process, too.

A project's `CONTRIBUTING.md` file will detail the project's code review processes.
All contributions require review from SAS project maintainers.
They may run unit tests, development tests, integrations tests, and security scans using internal SAS infrastructure.
In this case, they may not merge a contribution directly from GitHub; instead, they'll work with submissions internally first, vetting them to ensure they meet SAS standards.

We’ll always do our best to work with contributors in public issues and pull requests; however, to ensure our code meets our internal compliance standards, we may need to incorporate your submission into a solution we push ourselves.
And we work to ensure all contributors receive appropriate recognition for their contributions—at the very least, by acknowledging contributors in our release notes.
