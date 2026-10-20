# Git Cheat Sheet-1

**Source:** [`Git Cheat Sheet-1.docx`](../archive/canvas-submissions/Git%20Cheat%20Sheet-1.docx)  
**Course:** COSC 381 - Software Engineering Solutions (EMU)  
**Author:** Julio Barros

-s

--short

Give the output in the short-format.

-b

--branch

Show the branch and tracking info even in short-format.

--show-stash

Show the number of entries currently stashed away.

--porcelain[=<version>]

Give the output in an easy-to-parse format for scripts. This is similar to the short output, but will remain stable across Git versions and regardless of user configuration. See below for details.

The version parameter is used to specify the format version. This is optional and defaults to the original version v1 format.

--long

Give the output in the long-format. This is the default.

-v

--verbose

In addition to the names of files that have been changed, also show the textual changes that are staged to be committed (i.e., like the output of git diff --cached). If -v is specified twice, then also show the changes in the working tree that have not yet been staged (i.e., like the output of git diff).

-u[<mode>]

--untracked-files[=<mode>]

Show untracked files.

The mode parameter is used to specify the handling of untracked files. It is optional: it defaults to all, and if specified, it must be stuck to the option (e.g. -uno, but not -u no).

The possible options are:

no - Show no untracked files.

normal - Shows untracked files and directories.

all - Also shows individual files in untracked directories.

When -u option is not used, untracked files and directories are shown (i.e. the same as specifying normal), to help you avoid forgetting to add newly created files. Because it takes extra work to find untracked files in the filesystem, this mode may take some time in a large working tree. Consider enabling untracked cache and split index if supported (see git update-index --untracked-cache and git update-index --split-index), Otherwise you can use no to have git status return more quickly without showing untracked files.

The default can be changed using the status.showUntrackedFiles configuration variable documented in.

--ignore-submodules[=<when>]

Ignore changes to submodules when looking for changes. <when> can be either "none", "untracked", "dirty" or "all", which is the default. Using "none" will consider the submodule modified when it either contains untracked or modified files or its HEAD differs from the commit recorded in the superproject and can be used to override any settings of the ignore option. When "untracked" is used submodules are not considered dirty when they only contain untracked content (but they are still scanned for modified content). Using "dirty" ignores all changes to the work tree of submodules, only changes to the commits stored in the superproject are shown (this was the behavior before 1.7.0). Using "all" hides all changes to submodules (and suppresses the output of submodule summaries when the config option status.submoduleSummary is set).

--ignored[=<mode>]

Show ignored files as well.

The mode parameter is used to specify the handling of ignored files. It is optional: it defaults to traditional.

The possible options are:

traditional - Shows ignored files and directories, unless --untracked-files=all is specified, in which case individual files in ignored directories are displayed.

no - Show no ignored files.

matching - Shows ignored files and directories matching an ignore pattern.

When matching mode is specified, paths that explicitly match an ignored pattern are shown. If a directory matches an ignore pattern, then it is shown, but not paths contained in the ignored directory. If a directory does not match an ignore pattern, but all contents are ignored, then the directory is not shown, but all contents are shown.

-z

Terminate entries with NUL, instead of LF. This implies the --porcelain=v1 output format if no other format is given.

--column[=<options>]

--no-column

Display untracked files in columns. See configuration variable column.status for option syntax. --column and --no-column without options are equivalent to always and never respectively.

--ahead-behind

--no-ahead-behind

Display or do not display detailed ahead/behind counts for the branch relative to its upstream branch. Defaults to true.

--renames

--no-renames

Turn on/off rename detection regardless of user configuration.

--find-renames[=<n>]

Turn on rename detection, optionally setting the similarity threshold.
