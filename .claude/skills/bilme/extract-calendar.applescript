-- Extract Apple Calendar events for a given month/year.
-- Usage: osascript extract-calendar.applescript <MONTH 1-12> <YEAR>
-- Output: TSV (calendar<TAB>date<TAB>start<TAB>end<TAB>summary) — sorted by start date.

on run argv
	if (count of argv) is less than 2 then
		error "Usage: osascript extract-calendar.applescript <MONTH 1-12> <YEAR>"
	end if
	set theMonth to (item 1 of argv) as integer
	set theYear to (item 2 of argv) as integer

	set startDate to current date
	set year of startDate to theYear
	set month of startDate to theMonth
	set day of startDate to 1
	set hours of startDate to 0
	set minutes of startDate to 0
	set seconds of startDate to 0

	set endDate to startDate + (32 * days)
	set day of endDate to 1
	set hours of endDate to 0
	set minutes of endDate to 0
	set seconds of endDate to 0

	-- Only these calendars matter for Payfit timesheet:
	-- "Calendrier" = personal events
	-- "Jours fériés - France" = holidays
	set targetCalendars to {"Calendrier", "Jours fériés - France"}

	set output to ""
	tell application "Calendar"
		repeat with calName in targetCalendars
			try
				set cal to first calendar whose name is calName
				set theEvents to (every event of cal whose start date is greater than or equal to startDate and start date is less than endDate)
				repeat with anEvent in theEvents
					set evtSummary to summary of anEvent
					if evtSummary is missing value then set evtSummary to ""
					set evtStart to start date of anEvent
					set evtEnd to end date of anEvent
					set output to output & calName & tab & my isoDate(evtStart) & tab & my isoDateTime(evtStart) & tab & my isoDateTime(evtEnd) & tab & evtSummary & linefeed
				end repeat
			end try
		end repeat
	end tell
	return output
end run

on isoDate(d)
	set y to year of d as integer
	set m to (month of d as integer)
	set dd to day of d as integer
	return (y as text) & "-" & my pad(m) & "-" & my pad(dd)
end isoDate

on isoDateTime(d)
	set hh to hours of d as integer
	set mm to minutes of d as integer
	return my isoDate(d) & " " & my pad(hh) & ":" & my pad(mm)
end isoDateTime

on pad(n)
	if n < 10 then
		return "0" & (n as text)
	else
		return n as text
	end if
end pad
