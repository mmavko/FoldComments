import sublime, sublime_plugin

class FoldUnfoldCommentsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        comments = view.find_by_selector('comment')

        if view.fold(comments[0]):
            view.fold(comments)
        else:
            view.unfold(comments)
