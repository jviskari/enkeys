#converts exposurecheck log to simple CSV
jq '.ExposureChecks[] | {Timestamp,RandomIDCount} | [.Timestamp, .RandomIDCount] | @csv' $1 | awk -F '[\" ,]' {'print $3","$7 '}
