# Devly Affirmations

Affirmations for the qU1rkY dev in you ;)

## How to use?

This project is currently deployed at https://affirmations.gavindsouza.in. The site is pretty simple such that it returns a random affirmation each time you make a call. 

The best way to use this project is by consuming it from your favourite interface built for affirmations, which for me looks like:

```bash
~ curl -s https://affirmations.gavindsouza.in | fx 'x.affirmation' | cowsay
 ________________
< I am fullstack >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

```

## How to contribute?

To contribute affirmations, all you need to do is open an issue via the ["Affirmation Form"](//github.com/gavindsouza/devly-affirmations/issues/new?assignees=&labels=affirmation&template=submit_affirmation.yml) template. A "LGTM" comment from one of the maintainers will merge your contribution into the source 😁. Alternatively, you can choose to update the `affirmations.json` file manually.

A deploy is triggered on each push to the default branch. Special thanks to deta.sh for the hosting.

## License

The project is released under the [Apache 2.0](/LICENSE) license, and the affirmations are released under [CC-BY-NC-SA](/affirmations/LICENSE).