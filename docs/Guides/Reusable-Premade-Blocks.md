# Reusable premade blocks

A premade block is a saved graph template. Create it in the Sequence Editor by selecting the nodes to reuse. Importing it copies nodes into the open sequence so you can adjust them there.

## Save a selection

1. Build and test the fragment in the graph.
2. Hold **Shift** and drag a selection rectangle over the nodes to reuse.
3. With nodes selected, choose **Save Premade Block** in the top bar, or right-click and choose **Save as Premade Block**.
4. Give the template a unique name in the native dialog.

The Library receives a copy. Saving this selection does not replace the open sequence or its unsaved draft.

Only selected nodes and links between selected nodes are saved. Links crossing the selection boundary are not part of the template. Select a clear entry path; include a Watcher with its action path rather than saving an orphaned watcher action. Ambiguous fragments are rejected instead of silently flattening their control flow.

## Import a copy

Clear the selection to make the top button show **Import Premade Block**. Choose it to open the Library's **Blocks** pane, select a template, and choose **Import**.

The imported copy receives remapped graph identifiers. Check its block names, Step ID targets, external block references, variables, screen areas, images, and application targets before running it. Later edits to the copy do not update the saved template.

Variables are still part of the current playback. Include required Starter Variables in the selection or provide them in the destination sequence. A Reset Variable action requires a declared start value at runtime.

## Share a `.prm` file

In **Library -> Blocks**, select a template and choose **Save .prm**. On the receiving installation, **Load .prm** adds the template to that Library; then import it into an open sequence.

Images embedded in the selected nodes travel with the template. Missing file references must be corrected before selection save. The Library file operations preserve the currently open sequence.

Save the containing sequence separately with its normal library/file actions. See [editors and saving](../App-Features/Editors-And-Saving.md) and [blocks and Step IDs](../Basics/Blocks-And-Numbering.md).
