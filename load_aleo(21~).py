#!/usr/bin/env python3

import iterm2

async def main(connection):
    app = await iterm2.async_get_app(connection)
    window = app.current_window
    if window is not None:
        new_tab = await window.async_create_tab(profile="aleo021")
        session01 = new_tab.current_session
        if session01 is not None:
            await session01.async_split_pane(vertical=False, before=False, profile="aleo022")
            session02 = new_tab.sessions[-1]
            if session02 is not None:
                await session02.async_split_pane(vertical=False, before=False, profile="faleo023")
                session03 = new_tab.sessions[-1]
                if session03 is not None:
                    await session03.async_split_pane(vertical=True, before=False, profile="aleo091")
        if session01 is not None:
            await session01.async_split_pane(vertical=True, before=False, profile="aleo024")
        if session02 is not None:
            await session02.async_split_pane(vertical=True, before=False, profile="aleo090")

    else:
        print("No current window")

iterm2.run_until_complete(main)