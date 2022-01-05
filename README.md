# mqm2022 [![Netlify Status](https://api.netlify.com/api/v1/badges/1982dc57-e467-412e-8999-f846c9befcf4/deploy-status)](https://app.netlify.com/sites/zen-pasteur-fe2af0/deploys)

This is the website for the 2022 Molecular Quantum Mechanics conference at Virginia Tech.  The site is based on [Hugo](https://gohugo.io/), and CI (and eventually hosting) is handled by [Netlify](https://www.netlify.com/).  The site uses the eventre-hugo theme from [Themefisher](https://themefisher.com/) (which we obtained from [Gethugothemes](https://gethugothemes.com/)).

This site is very much under development, but we will deploy it soon at https://mqm2022.org/. 

Many thanks to [loriab](https://github.com/loriab) who set up the [Psi4](https://psicode.org) website using this infrastructure.  We learned lots from her examples.

## Get hugo

We use Mac OSX systems, and [homebrew](https://brew.sh/) is a simple method for obtaining hugo: `brew install hugo`

## Get website

Fork this repo, then clone it locally:
* `git clone --recursive https://github.com/<USERNAME>/mqm2022.git`
* `git remote add upstream https://github.com/CrawfordGroup/mqm2022`

## Create a local build of the website

* `cd mqm2022`
* `hugo server -D`
* View in a browser at http://localhost:1313/
