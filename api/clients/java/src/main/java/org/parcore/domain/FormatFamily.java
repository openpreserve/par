package org.parcore.domain;

import com.google.gson.annotations.SerializedName;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/**
 * A format family is simply a means of grouping more specific file formats into more general groups. These can be high level groupings such as Videos, Documents, etc, or more specific groupings such as JPEGs, Excel Spreadsheets, etc. It may even be used to group otherwise unrelated formats, to capture, for example, the set of accepted formats, for example, [PDF 1.4, TIFF, MKV, WAV], or to specify all formats, e.g. [ALL]. These can be formally specified, with a fixed ID and Namespace, or just a generic label
 */
@SuppressWarnings("unused")
@ApiModel(description = "A format family is simply a means of grouping more specific file formats into more general groups. These can be high level groupings such as Videos, Documents, etc, or more specific groupings such as JPEGs, Excel Spreadsheets, etc. It may even be used to group otherwise unrelated formats, to capture, for example, the set of accepted formats, for example, [PDF 1.4, TIFF, MKV, WAV], or to specify all formats, e.g. [ALL]. These can be formally specified, with a fixed ID and Namespace, or just a generic label")
public class FormatFamily {

    @SerializedName("familyType")
    private String familyType = null;

    @SerializedName("formats")
    private List<ParIdentifier> formats = null;

    @SerializedName("identifier")
    private ParIdentifier identifier = null;

    /**
     * Get familyType
     * @return familyType
     **/
    @ApiModelProperty(value = "")
    public String getFamilyType() {
        return familyType;
    }

    public void setFamilyType(String familyType) {
        this.familyType = familyType;
    }

    public void addFormatsItem(ParIdentifier formatsItem) {
        if (this.formats == null) {
            this.formats = new ArrayList<>();
        }
        this.formats.add(formatsItem);
    }

    /**
     * Get formats
     * @return formats
     **/
    @ApiModelProperty(value = "")
    public List<ParIdentifier> getFormats() {
        return formats;
    }

    public void setFormats(List<ParIdentifier> formats) {
        this.formats = formats;
    }

    /**
     * Get identifier
     * @return identifier
     **/
    @ApiModelProperty(value = "")
    public ParIdentifier getIdentifier() {
        return identifier;
    }

    public void setIdentifier(ParIdentifier identifier) {
        this.identifier = identifier;
    }


    @Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        FormatFamily formatFamily = (FormatFamily) o;
        return Objects.equals(this.familyType, formatFamily.familyType) &&
                Objects.equals(this.formats, formatFamily.formats) &&
                Objects.equals(this.identifier, formatFamily.identifier);
    }

    @Override
    public int hashCode() {
        return Objects.hash(familyType, formats, identifier);
    }


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class FormatFamily {\n");

        sb.append("    familyType: ").append(toIndentedString(familyType)).append("\n");
        sb.append("    formats: ").append(toIndentedString(formats)).append("\n");
        sb.append("    identifier: ").append(toIndentedString(identifier)).append("\n");
        sb.append("}");
        return sb.toString();
    }

    /**
     * Convert the given object to string with each line indented by 4 spaces
     * (except the first line).
     */
    private String toIndentedString(java.lang.Object o) {
        if (o == null) {
            return "null";
        }
        return o.toString().replace("\n", "\n    ");
    }

}
