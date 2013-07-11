import sublime, sublime_plugin

class FoldUnfoldCommentsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        comments = filter(lambda region: len(view.lines(region)) > 1, view.find_by_selector('comment'))

        if len(comments) > 0:
            if view.fold(comments[0]):
                view.fold(comments)
            else:
                view.unfold(comments)
