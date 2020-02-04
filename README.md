# CocoaPod Matcher
## 🤔 About
CocoaPod Matcher is a Homebrew package to assign missing version numbers to dependencies listed in a `Podfile`. It does so by scanning the `Podfile.lock` and assigning the installed version numbers back to the `Podfile`.

## ➡️💻 Installation
Installation is as simple as it always is with Homebrew packages. First just add the new tap
```bash
brew tap mapierce/homebrew-taps
```
And the install the package with
```bash
brew install cocoapod-matcher
```
And you’re good to go!

## 👩‍💻 How to use
As you would expect, you need a `Podfile`, and a `Podfile.lock` in the directory you run from, otherwise you’ll see the error:
```bash
A Podfile and/or a Podfile.lock were not found in the current directory
```
Once you do run from a suitable directory, your `Podfile` will automatically update.

## 👨‍👩‍👧‍👦 Contributing
If you run into any problems, please submit an issue. Pull requests are also welcome! By contributing to CocoaPod-Matcher you agree that your contributions will be licensed under its MIT license.

If CocoaPod-Matcher helps you out, I’d love to hear from you on  [Twitter](https://twitter.com/PierceMatthew) !

## 🙋‍♂️ Author
CocoaPod-Matcher was created by Matthew Pierce ( [@PierceMatthew](https://twitter.com/PierceMatthew) )

## 🔖 License
CocoaPod-Matcher is available under the MIT license. See the LICENSE file for more info.
