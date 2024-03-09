#!/usr/bin/env python3

import iterm2

async def main(connection):
    app = await iterm2.async_get_app(connection)
    window = app.current_window
    if window is not None:
        new_tab = await window.async_create_tab(profile="node-g0-01")
        session01 = new_tab.current_session
        if session01 is not None:
            await session01.async_split_pane(vertical=False, before=False, profile="node-g0-02")
            session02 = new_tab.sessions[-1]
            if session02 is not None:
                await session02.async_split_pane(vertical=True, before=False, profile="node-g0-04")
        if session01 is not None:
            await session01.async_split_pane(vertical=True, before=False, profile="node-g0-03")

    else:
        print("No current window")

iterm2.run_until_complete(main)